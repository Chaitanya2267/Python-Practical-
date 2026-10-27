"""
main.py - Patient Queue Management System (entry point + dashboard)

Educational demo project. Criticality ratings and recovery dates are entered
manually and are NOT clinical recommendations. Run with:  python main.py
"""

import csv
import tkinter as tk
from collections import Counter
from datetime import datetime, timedelta
from tkinter import ttk, messagebox, filedialog

import database as db
from patient_form import PatientForm, criticality_category, CRIT_COLORS

HOSPITAL_NAME = "City Care Hospital"

# ---- colour scheme (hospital blue / teal) ----
BG = "#F3F7FA"
SIDEBAR = "#0A3D55"
SIDEBAR_ACTIVE = "#12739A"
PRIMARY = "#0B5E7E"
WHITE = "#FFFFFF"

STATUS_BG = {db.WAITING: "#FFF4D6", db.IN_CONSULTATION: "#D9EEFF",
             db.COMPLETED: "#DDF5E3", db.CANCELLED: "#E6E6E6"}
STATUS_TAG = {s: "st_" + s.lower().replace(" ", "_") for s in db.ALL_STATUSES}
DOTS = {"Low": "●", "Moderate": "●●", "High": "●●●", "Very High": "●●●●"}

# (key, heading, width, anchor) for each table
PATIENT_COLS = [
    ("id", "Patient ID", 80, "center"), ("name", "Name", 150, "w"),
    ("age", "Age", 50, "center"), ("gender", "Gender", 70, "center"),
    ("date", "Entry Date", 95, "center"), ("time", "Entry Time", 80, "center"),
    ("recovery", "Recovery Days", 100, "center"), ("crit", "Criticality (1-10)", 140, "w"),
    ("queue", "Queue No.", 75, "center"), ("status", "Queue Status", 110, "center"),
    ("doctor", "Doctor", 110, "w"), ("wait", "Waiting", 85, "center")]
QUEUE_COLS = [
    ("queue", "Queue No.", 75, "center"), ("id", "Patient ID", 80, "center"),
    ("name", "Name", 150, "w"), ("age", "Age", 50, "center"),
    ("crit", "Criticality (1-10)", 140, "w"), ("time", "Entry Time", 80, "center"),
    ("wait", "Waiting", 90, "center"), ("doctor", "Doctor", 110, "w")]
DASH_COLS = [
    ("queue", "Queue No.", 75, "center"), ("id", "ID", 70, "center"),
    ("name", "Name", 150, "w"), ("crit", "Criticality", 120, "w"),
    ("wait", "Waiting", 90, "center")]


# ---------------------------------------------------------------- small helper functions
def entry_datetime(p):
    """Combine the stored entry date and time into one datetime object."""
    return datetime.strptime(f"{p['entry_date']} {p['entry_time']}", "%Y-%m-%d %H:%M:%S")


def waiting_minutes(p):
    """Minutes waited so far (only meaningful for Waiting patients)."""
    return max(0, int((datetime.now() - entry_datetime(p)).total_seconds() // 60))


def format_minutes(minutes):
    hours, mins = divmod(minutes, 60)
    return f"{mins} min" if hours == 0 else f"{hours}h {mins:02d}m"


def waiting_text(p):
    return format_minutes(waiting_minutes(p)) if p["status"] == db.WAITING else "-"


def recovery_date(p):
    """Estimated recovery date = entry date + expected recovery days (an ESTIMATE)."""
    return entry_datetime(p).date() + timedelta(days=p["recovery_days"])


def crit_text(p):
    category = criticality_category(p["criticality"])
    return f"{p['criticality']}  {DOTS[category]} {category}"


def pretty_date(text):
    return datetime.strptime(text, "%Y-%m-%d").strftime("%d %b %Y")


# ---------------------------------------------------------------- main application
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Patient Queue Management System")
        self.geometry("1280x780")
        self.minsize(1100, 680)
        self.configure(bg=BG)

        try:
            db.init_db()
            db.seed_sample_data()
        except db.DatabaseError as err:
            messagebox.showerror("Database Error", f"Could not open the database:\n{err}")
            self.destroy()
            raise SystemExit(1)

        self.search_text = ""
        self.setup_styles()
        self.build_sidebar()

        main = tk.Frame(self, bg=BG)
        main.grid(row=0, column=1, sticky="nsew")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)
        main.rowconfigure(2, weight=1)

        self.build_header(main)
        self.build_cards(main)

        container = tk.Frame(main, bg=BG)
        container.grid(row=2, column=0, sticky="nsew", padx=15, pady=(5, 5))
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)
        self.views = {}
        self.view_trees = {}
        for name, builder in (("Dashboard", self.build_dashboard_view),
                              ("Patients", self.build_patients_view),
                              ("Queue Management", self.build_queue_view),
                              ("Reports", self.build_reports_view)):
            frame = tk.Frame(container, bg=BG)
            frame.grid(row=0, column=0, sticky="nsew")
            self.views[name] = frame
            self.view_trees[name] = builder(frame)

        tk.Label(main, bg=BG, fg="#777777", font=("Segoe UI", 8, "italic"),
                 text="Educational demo only - criticality ratings and recovery dates are manual "
                      "estimates, not medical advice or triage.").grid(row=3, column=0, pady=(0, 6))

        self.show_view("Dashboard")
        self.update_clock()
        self.refresh_all()
        self.after(30000, self.auto_refresh)

    # ------------------------------------------------------------ styling
    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview", rowheight=28, font=("Segoe UI", 10), background=WHITE,
                        fieldbackground=WHITE)
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"),
                        background=PRIMARY, foreground="white")
        style.map("Treeview.Heading", background=[("active", SIDEBAR_ACTIVE)])
        style.map("Treeview", background=[("selected", "#2B8CBE")],
                  foreground=[("selected", "white")])
        style.configure("TLabelframe", background=BG)
        style.configure("TLabelframe.Label", background=BG, foreground=PRIMARY,
                        font=("Segoe UI", 10, "bold"))

    def button(self, parent, text, command, color=PRIMARY):
        return tk.Button(parent, text=text, command=command, bg=color, fg="white",
                         activebackground=SIDEBAR_ACTIVE, activeforeground="white",
                         relief="flat", padx=12, pady=6, cursor="hand2",
                         font=("Segoe UI", 9, "bold"))

    # ------------------------------------------------------------ sidebar / header / cards
    def build_sidebar(self):
        bar = tk.Frame(self, bg=SIDEBAR, width=200)
        bar.grid(row=0, column=0, sticky="ns")
        bar.grid_propagate(False)
        tk.Label(bar, text="+  CityCare", bg=SIDEBAR, fg="white",
                 font=("Segoe UI", 16, "bold")).pack(pady=(25, 30))
        self.nav_buttons = {}
        for name in ("Dashboard", "Patients", "Queue Management", "Reports"):
            btn = tk.Button(bar, text=f"   {name}", anchor="w", bg=SIDEBAR, fg="white",
                            activebackground=SIDEBAR_ACTIVE, activeforeground="white",
                            relief="flat", font=("Segoe UI", 11), pady=10, cursor="hand2",
                            command=lambda n=name: self.show_view(n))
            btn.pack(fill="x")
            self.nav_buttons[name] = btn

    def show_view(self, name):
        self.current_view = name
        self.views[name].tkraise()
        for key, btn in self.nav_buttons.items():
            btn.config(bg=SIDEBAR_ACTIVE if key == name else SIDEBAR)

    def build_header(self, parent):
        header = tk.Frame(parent, bg=PRIMARY)
        header.grid(row=0, column=0, sticky="ew")
        left = tk.Frame(header, bg=PRIMARY)
        left.pack(side="left", padx=20, pady=10)
        tk.Label(left, text="Patient Queue Management System", bg=PRIMARY, fg="white",
                 font=("Segoe UI", 18, "bold")).pack(anchor="w")
        tk.Label(left, text=f"{HOSPITAL_NAME} (sample name)", bg=PRIMARY, fg="#BEE3F8",
                 font=("Segoe UI", 11)).pack(anchor="w")
        tk.Label(left, text="Welcome, hospital staff! Have a smooth and productive shift.",
                 bg=PRIMARY, fg="white", font=("Segoe UI", 9, "italic")).pack(anchor="w")
        right = tk.Frame(header, bg=PRIMARY)
        right.pack(side="right", padx=20)
        self.date_label = tk.Label(right, bg=PRIMARY, fg="white", font=("Segoe UI", 11))
        self.date_label.pack(anchor="e")
        self.clock_label = tk.Label(right, bg=PRIMARY, fg="white", font=("Consolas", 24, "bold"))
        self.clock_label.pack(anchor="e")

    def update_clock(self):
        """Runs every second using Tkinter's after() method."""
        now = datetime.now()
        self.date_label.config(text=now.strftime("%A, %d %B %Y"))
        self.clock_label.config(text=now.strftime("%H:%M:%S"))
        self.after(1000, self.update_clock)

    def build_cards(self, parent):
        row = tk.Frame(parent, bg=BG)
        row.grid(row=1, column=0, sticky="ew", padx=15, pady=10)
        self.card_values = {}
        cards = [("total", "Total Patients", "#0B5E7E"), ("waiting", "Waiting", "#E0A800"),
                 ("consulting", "In Consultation", "#2B8CBE"), ("completed", "Completed", "#2E8B57"),
                 ("high", "High Criticality (7-10)", "#C62828")]
        for i, (key, title, color) in enumerate(cards):
            row.columnconfigure(i, weight=1, uniform="card")
            card = tk.Frame(row, bg=WHITE, highlightbackground="#D5DEE5", highlightthickness=1)
            card.grid(row=0, column=i, sticky="ew", padx=5)
            tk.Frame(card, bg=color, height=5).pack(fill="x")
            value = tk.Label(card, text="0", bg=WHITE, fg=color, font=("Segoe UI", 26, "bold"))
            value.pack(pady=(6, 0))
            tk.Label(card, text=title, bg=WHITE, fg="#555555", font=("Segoe UI", 10)).pack(pady=(0, 8))
            self.card_values[key] = value

    # ------------------------------------------------------------ table helpers
    def make_tree(self, parent, columns, height=10):
        """Create a Treeview with vertical + horizontal scrollbars."""
        frame = tk.Frame(parent, bg=BG)
        tree = ttk.Treeview(frame, columns=[c[0] for c in columns], show="headings",
                            height=height, selectmode="browse")
        for key, heading, width, anchor in columns:
            tree.heading(key, text=heading)
            tree.column(key, width=width, anchor=anchor, minwidth=50)
        vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(0, weight=1)
        for status, tag in STATUS_TAG.items():   # colour rows by status
            tree.tag_configure(tag, background=STATUS_BG[status])
        return frame, tree

    def fill_tree(self, tree, rows):
        """Replace the table contents but keep the selected patient selected."""
        selected = tree.selection()
        tree.delete(*tree.get_children())
        for iid, values, tag in rows:
            tree.insert("", "end", iid=iid, values=values, tags=(tag,))
        if selected and tree.exists(selected[0]):
            tree.selection_set(selected[0])

    def patient_row(self, p):
        values = (p["patient_id"], p["name"], p["age"], p["gender"], pretty_date(p["entry_date"]),
                  p["entry_time"], p["recovery_days"], crit_text(p), p["queue_number"],
                  p["status"], p["doctor"] or "-", waiting_text(p))
        return p["patient_id"], values, STATUS_TAG[p["status"]]

    def queue_row(self, p):
        values = (p["queue_number"], p["patient_id"], p["name"], p["age"], crit_text(p),
                  p["entry_time"], waiting_text(p), p["doctor"] or "-")
        return p["patient_id"], values, STATUS_TAG[p["status"]]

    def dash_row(self, p):
        values = (p["queue_number"], p["patient_id"], p["name"], crit_text(p), waiting_text(p))
        return p["patient_id"], values, STATUS_TAG[p["status"]]

    def selected_id(self):
        """ID of the patient selected in whichever view is currently showing."""
        for tree in self.view_trees[self.current_view]:
            if tree.selection():
                return tree.selection()[0]
        return None

    def require_selection(self):
        pid = self.selected_id()
        if pid is None:
            messagebox.showwarning("No Selection", "Please select a patient from the table first.")
        return pid

    def db_error(self, err):
        messagebox.showerror("Database Error", f"Something went wrong with the database:\n{err}")

    # ------------------------------------------------------------ views
    def build_dashboard_view(self, view):
        view.columnconfigure(0, weight=1, uniform="d")
        view.columnconfigure(1, weight=1, uniform="d")
        view.rowconfigure(1, weight=1)

        stats = ttk.LabelFrame(view, text="Today's Statistics", padding=10)
        stats.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 8))
        self.dash_stats = {}
        for i, (key, title) in enumerate((("today", "Registered today"),
                                          ("waiting", "Currently waiting"),
                                          ("longest", "Longest current wait"),
                                          ("average", "Average current wait"))):
            tk.Label(stats, text=title, bg=BG, fg="#555555").grid(row=0, column=i, padx=25)
            var = tk.StringVar(value="-")
            tk.Label(stats, textvariable=var, bg=BG, fg=PRIMARY,
                     font=("Segoe UI", 16, "bold")).grid(row=1, column=i, padx=25)
            self.dash_stats[key] = var
        actions = tk.Frame(stats, bg=BG)
        actions.grid(row=0, column=4, rowspan=2, padx=30)
        self.button(actions, "Call Next Patient", self.call_next, "#2E8B57").pack(side="left", padx=4)
        self.button(actions, "Add Patient", self.add_patient).pack(side="left", padx=4)
        self.button(actions, "Refresh", self.refresh_all, "#777777").pack(side="left", padx=4)

        box1 = ttk.LabelFrame(view, text="Now in Consultation", padding=6)
        box1.grid(row=1, column=0, sticky="nsew", padx=(0, 5))
        box2 = ttk.LabelFrame(view, text="Next in Queue (queue order)", padding=6)
        box2.grid(row=1, column=1, sticky="nsew", padx=(5, 0))
        for box in (box1, box2):
            box.rowconfigure(0, weight=1)
            box.columnconfigure(0, weight=1)
        f1, self.dash_consult_tree = self.make_tree(box1, DASH_COLS)
        f1.grid(sticky="nsew")
        f2, self.dash_wait_tree = self.make_tree(box2, DASH_COLS)
        f2.grid(sticky="nsew")
        return [self.dash_consult_tree, self.dash_wait_tree]

    def build_patients_view(self, view):
        view.columnconfigure(0, weight=1)
        view.rowconfigure(2, weight=1)

        bar1 = tk.Frame(view, bg=BG)
        bar1.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        tk.Label(bar1, text="Search (name or ID):", bg=BG).pack(side="left")
        self.search_var = tk.StringVar()
        entry = ttk.Entry(bar1, textvariable=self.search_var, width=24)
        entry.pack(side="left", padx=6)
        entry.bind("<Return>", lambda event: self.search())
        self.button(bar1, "Search", self.search).pack(side="left", padx=2)
        self.button(bar1, "Clear Search", self.clear_search, "#777777").pack(side="left", padx=2)
        tk.Label(bar1, text="   Filter:", bg=BG).pack(side="left")
        self.filter_var = tk.StringVar(value="All")
        combo = ttk.Combobox(bar1, textvariable=self.filter_var, state="readonly", width=16,
                             values=["All"] + db.ALL_STATUSES)
        combo.pack(side="left", padx=6)
        combo.bind("<<ComboboxSelected>>", lambda event: self.populate_patients())

        bar2 = tk.Frame(view, bg=BG)
        bar2.grid(row=1, column=0, sticky="ew", pady=(0, 6))
        for text, cmd, color in (("Add", self.add_patient, "#2E8B57"),
                                 ("Update", self.update_patient, PRIMARY),
                                 ("Delete", self.delete_patient, "#C62828"),
                                 ("View Details", self.view_details, PRIMARY),
                                 ("Call Next", self.call_next, "#2B8CBE"),
                                 ("Complete", self.complete_consultation, "#2E8B57"),
                                 ("Cancel Entry", self.cancel_entry, "#E0A800"),
                                 ("Refresh", self.refresh_all, "#777777"),
                                 ("Export CSV", self.export_csv, "#6A4C93")):
            self.button(bar2, text, cmd, color).pack(side="left", padx=2)

        frame, self.patients_tree = self.make_tree(view, PATIENT_COLS, height=12)
        frame.grid(row=2, column=0, sticky="nsew")
        self.patients_tree.bind("<<TreeviewSelect>>", lambda event: self.show_selected_summary())
        self.patients_tree.bind("<Double-1>", lambda event: self.view_details())

        info = tk.Frame(view, bg=WHITE, highlightbackground="#D5DEE5", highlightthickness=1)
        info.grid(row=3, column=0, sticky="ew", pady=(6, 0))
        self.summary_label = tk.Label(info, bg=WHITE, anchor="w", font=("Segoe UI", 9),
                                      text="Select a patient to see the recovery estimate.")
        self.summary_label.pack(side="left", padx=10, pady=6)
        self.crit_label = tk.Label(info, bg=WHITE, font=("Segoe UI", 10, "bold"))
        self.crit_label.pack(side="left", padx=5)
        return [self.patients_tree]

    def build_queue_view(self, view):
        view.columnconfigure(0, weight=1)
        view.rowconfigure(2, weight=3)
        view.rowconfigure(4, weight=2)
        tk.Label(view, bg=BG, fg=PRIMARY, font=("Segoe UI", 12, "bold"),
                 text="Waiting Queue (strict queue order - criticality does not change the order)"
                 ).grid(row=0, column=0, sticky="w")
        bar = tk.Frame(view, bg=BG)
        bar.grid(row=1, column=0, sticky="ew", pady=6)
        self.button(bar, "Call Next Patient", self.call_next, "#2E8B57").pack(side="left", padx=2)
        self.button(bar, "Complete Consultation", self.complete_consultation, "#2B8CBE").pack(side="left", padx=2)
        self.button(bar, "Cancel Queue Entry", self.cancel_entry, "#E0A800").pack(side="left", padx=2)
        self.button(bar, "Refresh", self.refresh_all, "#777777").pack(side="left", padx=2)
        f1, self.queue_wait_tree = self.make_tree(view, QUEUE_COLS, height=6)
        f1.grid(row=2, column=0, sticky="nsew")
        tk.Label(view, text="Currently In Consultation", bg=BG, fg=PRIMARY,
                 font=("Segoe UI", 12, "bold")).grid(row=3, column=0, sticky="w", pady=(8, 2))
        f2, self.queue_consult_tree = self.make_tree(view, QUEUE_COLS, height=4)
        f2.grid(row=4, column=0, sticky="nsew")
        return [self.queue_wait_tree, self.queue_consult_tree]

    def build_reports_view(self, view):
        view.columnconfigure(0, weight=1, uniform="r")
        view.columnconfigure(1, weight=1, uniform="r")
        view.rowconfigure(1, weight=1)
        self.report_text = tk.StringVar()
        tk.Label(view, textvariable=self.report_text, bg=BG, fg="#333333", justify="left",
                 font=("Segoe UI", 11)).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 8))
        box1 = ttk.LabelFrame(view, text="Patients by Queue Status", padding=6)
        box1.grid(row=1, column=0, sticky="nsew", padx=(0, 5))
        box2 = ttk.LabelFrame(view, text="Patients by Criticality Category (manual ratings)", padding=6)
        box2.grid(row=1, column=1, sticky="nsew", padx=(5, 0))
        for box in (box1, box2):
            box.rowconfigure(0, weight=1)
            box.columnconfigure(0, weight=1)
        f1, self.report_status_tree = self.make_tree(box1, [("name", "Status", 200, "w"), ("count", "Patients", 100, "center")])
        f1.grid(sticky="nsew")
        f2, self.report_crit_tree = self.make_tree(box2, [("name", "Category", 200, "w"), ("count", "Patients", 100, "center")])
        f2.grid(sticky="nsew")
        self.button(view, "Export Records to CSV", self.export_csv, "#6A4C93").grid(
            row=2, column=0, sticky="w", pady=8)
        return []

    # ------------------------------------------------------------ refreshing
    def refresh_all(self):
        """Reload records and recalculate every number on screen."""
        try:
            counts = db.get_counts()
            everyone = db.get_patients()
            shown = db.get_patients(self.search_text, self.status_filter())
        except db.DatabaseError as err:
            self.db_error(err)
            return
        waiting = [p for p in everyone if p["status"] == db.WAITING]
        consulting = [p for p in everyone if p["status"] == db.IN_CONSULTATION]

        # summary cards
        for key in ("total", "waiting", "consulting", "completed", "high"):
            self.card_values[key].config(text=str(counts[key]))

        # tables
        self.fill_tree(self.patients_tree, [self.patient_row(p) for p in shown])
        self.fill_tree(self.queue_wait_tree, [self.queue_row(p) for p in waiting])
        self.fill_tree(self.queue_consult_tree, [self.queue_row(p) for p in consulting])
        self.fill_tree(self.dash_wait_tree, [self.dash_row(p) for p in waiting[:8]])
        self.fill_tree(self.dash_consult_tree, [self.dash_row(p) for p in consulting])

        # today's statistics + waiting durations
        waits = [waiting_minutes(p) for p in waiting]
        self.dash_stats["today"].set(str(counts["today"]))
        self.dash_stats["waiting"].set(str(counts["waiting"]))
        self.dash_stats["longest"].set(format_minutes(max(waits)) if waits else "-")
        self.dash_stats["average"].set(format_minutes(sum(waits) // len(waits)) if waits else "-")

        # reports
        by_status = Counter(p["status"] for p in everyone)
        by_cat = Counter(criticality_category(p["criticality"]) for p in everyone)
        self.fill_tree(self.report_status_tree,
                       [(s, (s, by_status.get(s, 0)), STATUS_TAG[s]) for s in db.ALL_STATUSES])
        self.fill_tree(self.report_crit_tree,
                       [(c, (c, by_cat.get(c, 0)), STATUS_TAG[db.COMPLETED])
                        for c in ("Low", "Moderate", "High", "Very High")])
        average = (sum(p["recovery_days"] for p in everyone) / len(everyone)) if everyone else 0
        self.report_text.set(f"Total registered: {counts['total']}     Registered today: {counts['today']}"
                             f"     Average expected recovery: {average:.1f} days (manual estimates)")
        self.show_selected_summary()

    def auto_refresh(self):
        """Every 30 seconds so waiting durations stay up to date."""
        self.refresh_all()
        self.after(30000, self.auto_refresh)

    def status_filter(self):
        value = self.filter_var.get()
        return None if value == "All" else value

    def populate_patients(self):
        self.search_text = self.search_var.get().strip()
        self.refresh_all()

    def search(self):
        self.populate_patients()

    def clear_search(self):
        self.search_var.set("")
        self.filter_var.set("All")
        self.populate_patients()

    def show_selected_summary(self):
        selection = self.patients_tree.selection()
        if not selection:
            self.summary_label.config(text="Select a patient to see the recovery estimate.")
            self.crit_label.config(text="")
            return
        try:
            p = db.get_patient(selection[0])
        except db.DatabaseError:
            return
        if p is None:
            return
        category = criticality_category(p["criticality"])
        self.summary_label.config(
            text=f"{p['name']} ({p['patient_id']})  |  Entry: {pretty_date(p['entry_date'])}  |  "
                 f"Expected recovery: {p['recovery_days']} days  |  "
                 f"Estimated recovery date: {recovery_date(p).strftime('%d %b %Y')} (estimate only)  |  Criticality:")
        self.crit_label.config(text=f"{p['criticality']} - {category}", fg=CRIT_COLORS[category])

    # ------------------------------------------------------------ actions
    def add_patient(self):
        PatientForm(self, self.save_patient)

    def save_patient(self, data, patient_id):
        """Called by the form. Returns True when saved so the form can close."""
        try:
            if patient_id is None:
                saved = db.add_patient(data)
                messagebox.showinfo("Patient Added",
                                    f"{saved['name']} registered.\nPatient ID: {saved['patient_id']}\n"
                                    f"Queue number: {saved['queue_number']}")
            else:
                db.update_patient(patient_id, data)
        except db.DatabaseError as err:
            self.db_error(err)
            return False
        self.refresh_all()
        return True

    def update_patient(self):
        pid = self.require_selection()
        if pid is None:
            return
        try:
            patient = db.get_patient(pid)
        except db.DatabaseError as err:
            self.db_error(err)
            return
        if patient:
            PatientForm(self, self.save_patient, patient)

    def delete_patient(self):
        pid = self.require_selection()
        if pid is None:
            return
        if messagebox.askyesno("Confirm Delete", f"Delete patient {pid} permanently?"):
            try:
                db.delete_patient(pid)
            except db.DatabaseError as err:
                self.db_error(err)
                return
            self.refresh_all()

    def call_next(self):
        try:
            patient = db.call_next()
        except db.DatabaseError as err:
            self.db_error(err)
            return
        if patient is None:
            messagebox.showinfo("Queue Empty", "No patients are currently waiting.")
            return
        messagebox.showinfo("Next Patient", f"Now calling: {patient['name']} "
                            f"(Queue No. {patient['queue_number']}).\nStatus set to In Consultation.")
        self.refresh_all()

    def complete_consultation(self):
        pid = self.require_selection()
        if pid is None:
            return
        try:
            patient = db.get_patient(pid)
            if patient["status"] != db.IN_CONSULTATION:
                messagebox.showwarning("Cannot Complete",
                                       "Only patients who are In Consultation can be marked Completed.")
                return
            db.set_status(pid, db.COMPLETED)
        except db.DatabaseError as err:
            self.db_error(err)
            return
        self.refresh_all()

    def cancel_entry(self):
        pid = self.require_selection()
        if pid is None:
            return
        try:
            patient = db.get_patient(pid)
            if patient["status"] in (db.COMPLETED, db.CANCELLED):
                messagebox.showwarning("Cannot Cancel",
                                       f"This visit is already {patient['status']}.")
                return
            if messagebox.askyesno("Confirm Cancel", f"Cancel the queue entry for {patient['name']}?"):
                db.set_status(pid, db.CANCELLED)
        except db.DatabaseError as err:
            self.db_error(err)
            return
        self.refresh_all()

    def view_details(self):
        pid = self.require_selection()
        if pid is None:
            return
        try:
            p = db.get_patient(pid)
        except db.DatabaseError as err:
            self.db_error(err)
            return
        if p is None:
            return
        win = tk.Toplevel(self)
        win.title(f"Patient Details - {p['patient_id']}")
        win.configure(bg=BG, padx=20, pady=15)
        win.resizable(False, False)
        win.transient(self)
        tk.Label(win, text=p["name"], bg=BG, fg=PRIMARY, font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 10))
        rows = [("Patient ID", p["patient_id"]), ("Age", p["age"]), ("Gender", p["gender"]),
                ("Entry Date", pretty_date(p["entry_date"])), ("Entry Time", p["entry_time"]),
                ("Expected Recovery Days", p["recovery_days"]),
                ("Estimated Recovery Date", f"{recovery_date(p).strftime('%d %b %Y')}  (estimate only)"),
                ("Criticality Rating", crit_text(p)), ("Queue Number", p["queue_number"]),
                ("Queue Status", p["status"]), ("Waiting Duration", waiting_text(p)),
                ("Assigned Doctor", p["doctor"] or "Not assigned")]
        for i, (label, value) in enumerate(rows, start=1):
            tk.Label(win, text=label + ":", bg=BG, fg="#555555", anchor="w").grid(
                row=i, column=0, sticky="w", pady=2, padx=(0, 20))
            tk.Label(win, text=str(value), bg=BG, font=("Segoe UI", 10, "bold"), anchor="w").grid(
                row=i, column=1, sticky="w", pady=2)
        tk.Label(win, bg=BG, fg="#777777", font=("Segoe UI", 8, "italic"),
                 text="Demo data only. Recovery date and rating are manual estimates,\n"
                      "not a medical prediction or recommendation.").grid(
                 row=len(rows) + 1, column=0, columnspan=2, pady=(10, 5))
        self.button(win, "Close", win.destroy, "#777777").grid(row=len(rows) + 2, column=0, columnspan=2)

    def export_csv(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV files", "*.csv")],
            initialfile=f"patients_{datetime.now():%Y%m%d_%H%M}.csv", title="Export patient records")
        if not path:
            return
        try:
            patients = db.get_patients()
            with open(path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Patient ID", "Name", "Age", "Gender", "Entry Date", "Entry Time",
                                 "Expected Recovery Days", "Estimated Recovery Date",
                                 "Criticality Rating", "Criticality Category", "Queue Number",
                                 "Queue Status", "Assigned Doctor"])
                for p in patients:
                    writer.writerow([p["patient_id"], p["name"], p["age"], p["gender"],
                                     p["entry_date"], p["entry_time"], p["recovery_days"],
                                     recovery_date(p).isoformat(), p["criticality"],
                                     criticality_category(p["criticality"]), p["queue_number"],
                                     p["status"], p["doctor"]])
        except (db.DatabaseError, OSError) as err:
            messagebox.showerror("Export Failed", f"Could not export records:\n{err}")
            return
        messagebox.showinfo("Export Complete", f"{len(patients)} records saved to:\n{path}")


if __name__ == "__main__":
    App().mainloop()
