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

# ------------------------------------------------------------------------------------------------

# Multilevel inheritance with private & protected

class Grandparent:
    def __init__(self):
        self._protected_var = "Protected from Grandparent"
        self.__private_var = "Private from Grandparent"

    def _protected_method(self):
        print("Protected method in Grandparent")

    def __private_method(self):
        print("Private method in Grandparent")

    def access_private(self):
        # Public accessor for private members
        print(self.__private_var)
        self.__private_method()

class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self._protected_var = "Protected overridden in Parent"
        self.__private_var = "Private in Parent"

    def _protected_method(self):
        print("Protected method in Parent")

    def access_private(self):
        print(self.__private_var)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self._protected_var = "Protected overridden in Child"
        self.__private_var = "Private in Child"

    def show(self):
        # Access protected variable
        print("Accessing protected:", self._protected_var)
        self._protected_method()

        # Access private via accessor
        self.access_private()

obj = Child()
obj.show()
obj.access_private()   # Calls Child’s private accessor