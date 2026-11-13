class Parent:
    def display(self):
        print("this is parent class")

class Child(Parent):
    def show(self):
        print("this is child class")

obj = Child()

obj.display()
obj.show()