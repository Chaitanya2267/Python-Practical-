# class Student:
#     def __init__(self, name, roll_no):
#         print("Constructor called")
#         self.name = name
#         self.roll_name = roll_no
# s1 = Student("csw", 13)
# print(s1.name, s1.roll_name)

class Student:
    def __init__(self, name):
        print("Constructor called")
        self.name = name

    def __del__(self):
        print("Destructor called for", self.name)

s1 = Student("Csw")
del s1