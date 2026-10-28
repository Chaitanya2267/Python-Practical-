# Button Example

from tkinter import *

root = Tk()


root.title("Button")
root.geometry("300x200")

def show():print("Button clicked")

# Button
btn = Button(root, text="Click Me", command=show)

# Label
lbl = Label(root, text="Label - Welcome to Python")
lbl.pack()
btn.pack()

# Entry
Label(root, text="Enter Name").pack()

e = Entry(root)
e.pack()

def show():print(e.get())

Button(root, text="Submit", command=show).pack()


v = IntVar()

Checkbutton(root, text="I agree",variable=v).pack()

def show():print(v.get())
Button(root, text="Submit", command=show).pack()

root.mainloop()
