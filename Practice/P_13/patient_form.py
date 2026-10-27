"""
patient_form.py - popup form used for adding and editing patients,
plus the input-validation and criticality helpers.
"""

import tkinter as tk
from tkinter import ttk, messagebox

from database import ALL_STATUSES, WAITING

# Colour used for each criticality category
CRIT_COLORS = {"Low": "#2E8B57", "Moderate": "#B8860B",
               "High": "#E06A00", "Very High": "#C62828"}


def criticality_category(rating):
    """1-3 Low, 4-6 Moderate, 7-8 High, 9-10 Very High."""
    if rating <= 3:
        return "Low"
    if rating <= 6:
        return "Moderate"
    if rating <= 8:
        return "High"
    return "Very High"


def _to_int(text):
    """Convert text to int, or return None if it is not a whole number."""
    try:
        return int(str(text).strip())
    except ValueError:
        return None


def validate_patient_input(name, age, gender, recovery, rating):
    """Check every field. Returns (clean_data, None) or (None, error_message)."""
    name = name.strip()
    if not name:
        return None, "Patient name cannot be empty."
    age_value = _to_int(age)
    if age_value is None or age_value <= 0 or age_value > 120:
        return None, "Age must be a positive whole number (1-120)."
    if gender not in ("Male", "Female", "Other"):
        return None, "Please select a gender."
    recovery_value = _to_int(recovery)
    if recovery_value is None or recovery_value <= 0:
        return None, "Expected recovery days must be a positive integer."
    rating_value = _to_int(rating)
    if rating_value is None or not 1 <= rating_value <= 10:
        return None, "Criticality rating must be an integer between 1 and 10."
    return {"name": name, "age": age_value, "gender": gender,
            "recovery_days": recovery_value, "criticality": rating_value}, None


class PatientForm(tk.Toplevel):
    """Modal window. `on_save(data, patient_id)` must return True if saving worked."""

    def __init__(self, parent, on_save, patient=None):
        super().__init__(parent)
        self.on_save = on_save
        self.patient = patient            # None -> add mode, dict -> edit mode
        self.title("Edit Patient" if patient else "Add New Patient")
        self.configure(bg="#F3F7FA", padx=20, pady=15)
        self.resizable(False, False)

        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.recovery_var = tk.StringVar()
        self.rating_var = tk.StringVar()
        self.doctor_var = tk.StringVar()
        self.status_var = tk.StringVar(value=WAITING)

        tk.Label(self, text=self.title(), font=("Segoe UI", 15, "bold"),
                 bg="#F3F7FA", fg="#0B5E7E").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        id_text = patient["patient_id"] if patient else "Auto-generated"
        self._row(1, "Patient ID", ttk.Label(self, text=id_text, font=("Segoe UI", 10, "bold")))
        self._row(2, "Patient Name *", ttk.Entry(self, textvariable=self.name_var, width=30))
        self._row(3, "Age *", ttk.Entry(self, textvariable=self.age_var, width=30))
        self._row(4, "Gender *", ttk.Combobox(self, textvariable=self.gender_var, width=27,
                  values=["Male", "Female", "Other"], state="readonly"))
        self._row(5, "Expected Recovery Days *", ttk.Entry(self, textvariable=self.recovery_var, width=30))
        self._row(6, "Criticality Rating (1-10) *", ttk.Spinbox(self, from_=1, to=10,
                  textvariable=self.rating_var, width=28))
        self.category_label = tk.Label(self, text="", bg="#F3F7FA", font=("Segoe UI", 10, "bold"))
        self.category_label.grid(row=7, column=1, sticky="w")
        self._row(8, "Assigned Doctor (optional)", ttk.Entry(self, textvariable=self.doctor_var, width=30))
        if patient:  # status can only be edited for existing patients
            self._row(9, "Queue Status", ttk.Combobox(self, textvariable=self.status_var, width=27,
                      values=ALL_STATUSES, state="readonly"))

        tk.Label(self, text="Rating is entered manually (demo only) - not clinical advice.",
                 bg="#F3F7FA", fg="#666666", font=("Segoe UI", 8, "italic")).grid(
                 row=10, column=0, columnspan=2, pady=(8, 0))

        buttons = tk.Frame(self, bg="#F3F7FA")
        buttons.grid(row=11, column=0, columnspan=2, pady=(12, 0))
        for text, cmd, color in (("Save", self.save, "#2E8B57"),
                                 ("Clear Form", self.clear_form, "#E0A800"),
                                 ("Cancel", self.destroy, "#777777")):
            tk.Button(buttons, text=text, command=cmd, bg=color, fg="white", relief="flat",
                      padx=14, pady=5, cursor="hand2").pack(side="left", padx=5)

        self.rating_var.trace_add("write", lambda *args: self.update_category())
        if patient:
            self.fill_from_patient()

        self.transient(parent)
        self.grab_set()            # block the main window until this one closes
        self.bind("<Return>", lambda event: self.save())

    def _row(self, row, label, widget):
        tk.Label(self, text=label, bg="#F3F7FA", anchor="w").grid(
            row=row, column=0, sticky="w", pady=4, padx=(0, 12))
        widget.grid(row=row, column=1, sticky="w", pady=4)

    def fill_from_patient(self):
        p = self.patient
        self.name_var.set(p["name"])
        self.age_var.set(p["age"])
        self.gender_var.set(p["gender"])
        self.recovery_var.set(p["recovery_days"])
        self.rating_var.set(p["criticality"])
        self.doctor_var.set(p["doctor"] or "")
        self.status_var.set(p["status"])

    def clear_form(self):
        """Reset every input field."""
        for var in (self.name_var, self.age_var, self.gender_var,
                    self.recovery_var, self.rating_var, self.doctor_var):
            var.set("")
        self.status_var.set(WAITING)

    def update_category(self):
        """Show Low / Moderate / High / Very High next to the rating."""
        try:
            rating = int(self.rating_var.get())
        except ValueError:
            rating = 0
        if 1 <= rating <= 10:
            category = criticality_category(rating)
            self.category_label.config(text=category, fg=CRIT_COLORS[category])
        else:
            self.category_label.config(text="")

    def save(self):
        data, error = validate_patient_input(
            self.name_var.get(), self.age_var.get(), self.gender_var.get(),
            self.recovery_var.get(), self.rating_var.get())
        if error:
            messagebox.showerror("Invalid Input", error, parent=self)
            return
        data["doctor"] = self.doctor_var.get().strip()
        data["status"] = self.status_var.get()
        patient_id = self.patient["patient_id"] if self.patient else None
        if self.on_save(data, patient_id):
            self.destroy()
