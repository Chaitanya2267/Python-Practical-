"""
database.py - SQLite storage layer for the Patient Queue Management System.

All SQL lives in this file so the GUI code (main.py) never touches the
database directly. Every query is parameterized (uses ? placeholders).
Educational demo only - fictional data, no real medical use.
"""

import os
import sqlite3
from contextlib import closing
from datetime import datetime, timedelta

# The database file is created next to this script.
DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "patients.db")

# Queue status values used everywhere in the project
WAITING = "Waiting"
IN_CONSULTATION = "In Consultation"
COMPLETED = "Completed"
CANCELLED = "Cancelled"
ALL_STATUSES = [WAITING, IN_CONSULTATION, COMPLETED, CANCELLED]


class DatabaseError(Exception):
    """Raised when anything goes wrong with the database."""


def _execute(sql, params=(), fetch="none"):
    """Run one SQL statement safely.

    fetch = "none" -> return number of rows changed
            "one"  -> return one row as a dict (or None)
            "all"  -> return a list of dicts
    """
    try:
        with closing(sqlite3.connect(DB_FILE)) as conn:
            conn.row_factory = sqlite3.Row
            with conn:  # commits on success, rolls back on error
                cur = conn.execute(sql, params)
                if fetch == "all":
                    return [dict(r) for r in cur.fetchall()]
                if fetch == "one":
                    row = cur.fetchone()
                    return dict(row) if row else None
                return cur.rowcount
    except sqlite3.Error as err:
        raise DatabaseError(str(err)) from err


# ---------------------------------------------------------------- setup
def init_db():
    """Create the tables if they do not exist yet."""
    _execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id     TEXT PRIMARY KEY,
            name           TEXT NOT NULL,
            age            INTEGER NOT NULL,
            gender         TEXT NOT NULL,
            entry_date     TEXT NOT NULL,   -- YYYY-MM-DD
            entry_time     TEXT NOT NULL,   -- HH:MM:SS
            recovery_days  INTEGER NOT NULL,
            criticality    INTEGER NOT NULL,
            queue_number   INTEGER NOT NULL,
            status         TEXT NOT NULL,
            doctor         TEXT DEFAULT ''
        )""")
    _execute("CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)")


def seed_sample_data():
    """Insert fictional sample patients ONCE (a flag in the meta table
    stops duplicates on every restart, even if the user deletes them all)."""
    if _execute("SELECT value FROM meta WHERE key = 'sample_loaded'", fetch="one"):
        return
    if get_counts()["total"] == 0:
        now = datetime.now()
        samples = [  # name, age, gender, minutes ago, recovery days, rating, status, doctor
            ("Aarav Sharma", 34, "Male", 180, 7, 3, COMPLETED, "Dr. Mehta"),
            ("Priya Nair", 52, "Female", 95, 14, 7, IN_CONSULTATION, "Dr. Rao"),
            ("Rohan Patil", 28, "Male", 70, 5, 2, WAITING, ""),
            ("Sneha Kulkarni", 61, "Female", 45, 21, 9, WAITING, "Dr. Rao"),
            ("Imran Shaikh", 19, "Male", 30, 3, 4, WAITING, ""),
            ("Neha Joshi", 43, "Female", 120, 10, 5, CANCELLED, "Dr. Mehta"),
        ]
        for number, s in enumerate(samples, start=1):
            entry = now - timedelta(minutes=s[3])
            _execute(
                "INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                (f"P{number:03d}", s[0], s[1], s[2], entry.strftime("%Y-%m-%d"),
                 entry.strftime("%H:%M:%S"), s[4], s[5], number, s[6], s[7]))
    _execute("INSERT INTO meta (key, value) VALUES ('sample_loaded', '1')")


# ---------------------------------------------------------------- helpers
def next_patient_id():
    """Generate the next unique ID: P001, P002, ..."""
    row = _execute("SELECT MAX(CAST(SUBSTR(patient_id, 2) AS INTEGER)) AS m FROM patients",
                   fetch="one")
    return f"P{(row['m'] or 0) + 1:03d}"


def next_queue_number():
    row = _execute("SELECT MAX(queue_number) AS m FROM patients", fetch="one")
    return (row["m"] or 0) + 1


# ---------------------------------------------------------------- CRUD
def add_patient(data):
    """Add a new patient. Returns the saved record (with ID and queue number)."""
    pid = next_patient_id()
    if get_patient(pid):  # extra safety: never reuse an ID
        raise DatabaseError(f"Duplicate patient ID: {pid}")
    now = datetime.now()
    _execute(
        "INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (pid, data["name"], data["age"], data["gender"],
         now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"),
         data["recovery_days"], data["criticality"],
         next_queue_number(), WAITING, data.get("doctor", "")))
    return get_patient(pid)


def get_patient(patient_id):
    return _execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,), fetch="one")


def get_patients(search="", status=None):
    """Return patients in queue order, optionally filtered by search text / status."""
    sql = "SELECT * FROM patients WHERE 1=1"
    params = []
    if search:
        sql += " AND (name LIKE ? OR patient_id LIKE ?)"
        params += [f"%{search}%", f"%{search}%"]
    if status:
        sql += " AND status = ?"
        params.append(status)
    sql += " ORDER BY queue_number ASC"
    return _execute(sql, tuple(params), fetch="all")


def update_patient(patient_id, data):
    changed = _execute(
        """UPDATE patients SET name=?, age=?, gender=?, recovery_days=?,
           criticality=?, doctor=?, status=? WHERE patient_id=?""",
        (data["name"], data["age"], data["gender"], data["recovery_days"],
         data["criticality"], data.get("doctor", ""), data["status"], patient_id))
    if changed == 0:
        raise DatabaseError("Patient not found.")


def delete_patient(patient_id):
    _execute("DELETE FROM patients WHERE patient_id = ?", (patient_id,))


# ---------------------------------------------------------------- queue
def set_status(patient_id, status):
    _execute("UPDATE patients SET status = ? WHERE patient_id = ?", (status, patient_id))


def call_next():
    """Call the waiting patient with the lowest queue number (pure queue order -
    criticality is NOT used). Returns the patient, or None if nobody is waiting."""
    row = _execute("SELECT * FROM patients WHERE status = ? ORDER BY queue_number ASC LIMIT 1",
                   (WAITING,), fetch="one")
    if row is None:
        return None
    set_status(row["patient_id"], IN_CONSULTATION)
    return get_patient(row["patient_id"])


# ---------------------------------------------------------------- statistics
def get_counts():
    """All the numbers for the summary cards in one query."""
    today = datetime.now().strftime("%Y-%m-%d")
    row = _execute(
        """SELECT COUNT(*) AS total,
                  SUM(status = ?) AS waiting,
                  SUM(status = ?) AS consulting,
                  SUM(status = ?) AS completed,
                  SUM(status = ?) AS cancelled,
                  SUM(criticality >= 7) AS high,
                  SUM(entry_date = ?) AS today
           FROM patients""",
        (WAITING, IN_CONSULTATION, COMPLETED, CANCELLED, today), fetch="one")
    return {key: (value or 0) for key, value in row.items()}
