
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()


root.title("Tkinter GUI")
root.geometry("500x550")

# 1. pack() example
pack_frame = tk.LabelFrame(root, text="Pack Example")
pack_frame.pack(fill="x", padx=10, pady=5)

tk.Label(pack_frame, text="Welcome to Tkinter").pack()
tk.Button(pack_frame, text="Click Me", command=lambda: messagebox.showinfo("Message", "Button Clicked!")).pack()

# 2. grid() example
grid_frame = tk.LabelFrame(root, text="Grid Example")
grid_frame.pack(fill="x", padx=10, pady=5)

tk.Label(grid_frame, text="Enter Your Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(grid_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# 3. place() example
place_frame = tk.LabelFrame(root, text="Place Example", height=100)
place_frame.pack(fill="x", padx=10, pady=5)
place_frame.pack_propagate(False)

tk.Button(place_frame, text="Button 1").place(x=30, y=20)
tk.Button(place_frame, text="Button 2").place(x=150, y=20)
tk.Button(place_frame, text="Button 3").place(x=270, y=20)

# 4. Radiobutton example
radio_frame = tk.LabelFrame(root, text="Radiobutton Example")
radio_frame.pack(fill="x", padx=10, pady=5)

gender = tk.StringVar(value="Male")

tk.Radiobutton(radio_frame, text="Male", variable=gender, value="Male").pack(side="left")
tk.Radiobutton(radio_frame, text="Female", variable=gender, value="Female").pack(side="left")

# 5. Checkbutton example
check_frame = tk.LabelFrame(root, text="Checkbutton Example")
check_frame.pack(fill="x", padx=10, pady=5)

python_var = tk.IntVar()
java_var = tk.IntVar()

tk.Checkbutton(check_frame, text="Python", variable=python_var).pack(side="left")
tk.Checkbutton(check_frame, text="Java", variable=java_var).pack(side="left")

# 6. Submit button
def submit():
    name = name_entry.get()
    selected_gender = gender.get()
    languages = []

    if python_var.get():
        languages.append("Python")
    if java_var.get():
        languages.append("Java")

    messagebox.showinfo(
        "Your Details",
        f"Name: {name}\n"
        f"Gender: {selected_gender}\n"
        f"Languages: {', '.join(languages) if languages else 'None'}"
    )

tk.Button(root, text="Submit", command=submit).pack(pady=10)

root.mainloop()
