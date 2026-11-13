# method overriding
# When a child class defines a method with the same name as a method in its parent class, it overrides that method.

class Parent:
    def display(self):
        print("this is parent class")
    
class Child:
    def display(self):
        print("this is child class")

p = Parent()
c = Child()

p.display()
c.display()