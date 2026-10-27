# Patient Queue Management System (Educational Demo)

A beginner-friendly desktop app built with **Python, Tkinter/ttk and SQLite**.
It manages patient records, queue order, manual criticality ratings and estimated
recovery dates for a fictional hospital ("City Care Hospital").

> **Not a medical system.** Criticality ratings and recovery dates are typed in by staff
> and are not clinical recommendations. Queue order never depends on the rating.
> All sample data is fictional.

## Files
| File | Purpose |
|---|---|
| `main.py` | Entry point, dashboard, all screens and button actions |
| `database.py` | SQLite setup, CRUD, queue and statistics queries |
| `patient_form.py` | Add/Edit popup form, validation, criticality categories |
| `patients.db` | Created automatically on first run |

## Run in VS Code
1. Install Python 3.8+ (tick "Add to PATH"; Tkinter is included on Windows/macOS).
   On Ubuntu/Debian: `sudo apt install python3-tk`.
2. In VS Code: **File > Open Folder** and choose this folder. Install the *Python* extension.
3. Open `main.py` and press the **Run** button, or in the terminal (`Ctrl+``):
   ```
   python main.py
   ```
   (use `python3 main.py` on macOS/Linux).
4. To reset the data, close the app and delete `patients.db`.

No `pip install` is needed - only built-in modules are used.

## Criticality categories
1-3 Low, 4-6 Moderate, 7-8 High, 9-10 Very High (dots show the level in tables).
