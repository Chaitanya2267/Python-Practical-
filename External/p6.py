import tkinter as tk 

root = tk.Tk()

root.title("My first GUI")
root.geometry("400x300")

label = tk.Label(root, text="Welcome to Python GUI")
label.pack()

def display():
    label.config(text="Button Clicked")

button = tk.Button(root, text="Click me", command=display)
button.pack()

root.mainloop()