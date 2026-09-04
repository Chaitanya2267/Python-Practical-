# 1. Single Inheritance

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# class Result(Student):
#     def display(self):
#         print(f"Name: {self.name}, Marks: {self.marks}")

# obj = Result("CSW", 85)
# obj.display()

# ----------------------------------------------------------------

# 2. Multiple Inheritance 

# class Sports:
#     def sport_marks(self):
#         return 20
    
# class Acedemics:
#     def academic_marks(self):
#         return 80

# class Student(Sports, Acedemics):
#     def total(self, name):
#         marks = self.sport_marks() + self.academic_marks()
#         print(f"Name: {name}, Total Marks: {marks}")

# obj = Student()
# obj.total("csw")

# ----------------------------------------------------------------

# 3. Multi-level inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks

# class Result(Student):
#     def show(self):
#         print(f"Name: {self.name}, Marks: {self.marks}")

# obj = Result("csw", 93)
# obj.show()

# ----------------------------------------------------------------

# 4. Hierachical Inheritance

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

# class Science(Student):
#     def display(self): 
#         print(f"Science student: {self.name}, Marks: {self.marks}")

# class Commerce(Student):
#     def display(self):
#         print(f"Commerce Student: {self.name}, Marks: {self.marks}")

# s1 = Science("csw", 88)
# c1 = Commerce("sw", 79)

# s1.display()
# c1.display()

# ----------------------------------------------------------------

# 5. Hybrid Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Academics(Person):
#     def __init__(self, name, marks):
#         super().__init__(name)
#         self.marks = marks

# class Sports(Person):
#     def __init__(self, name, sport_marks):
#         super().__init__(name)
#         self.sport_marks = sport_marks

# class Student(Academics, Sports):
#     def __init__(self, name, marks, sport_marks):
#         Academics.__init__(self, name, marks)
#         Sports.__init__(self, name, sport_marks)

#     def total(self):
#         print(f"Name: {self.name}, Total Marks: {self.marks + self.sport_marks}")

# obj = Student("Chaitanya", 85, 15)
# obj.total()