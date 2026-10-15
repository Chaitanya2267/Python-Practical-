# class student:
#     def display(self):
#         print("welcome")
# s1 = student()
# s1.display()

# class student:
#     def set_details(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def display_details(self):
#         print("student name:", self.name)
#         print("roll number:", self.roll_no)
#         print("marks:", self.marks)
# s1 = student()
# s1.set_details("csw", 13, 93)
# s1.display_details()

# class student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks
#     def display(self):
#         print("name:", self.name)
#         print("roll num:", self.roll_no)
#         print("marks:", self.marks)
# s1 = student("csw", 13, 93)
# s1.display()

# class student:
#     def __init__(self, name):
#         self.name = name
#         print("student created:", self.name)
#     def __del__(self):
#         print("destructor called", self.name)
# s1 = student("csw")
# del s1

