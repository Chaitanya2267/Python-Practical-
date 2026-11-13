class Student:
    # constructor
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("name:", self.name)
        print("roll no:", self.roll_no)
        print("marks", self.marks)

s1 = Student("csw", 13, 67)
s1.display()