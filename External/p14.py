class Parent:
    def display(self):
        print("this is parent")

class Child1(Parent):
    def show1(self):
        print("this is child 1")

class Child2(Parent):
    def show2(self):
        print("this is child 2")

obj1 = Child1()
obj2 = Child2()

obj1.display()
obj1.show1()

obj2.display()
obj2.show2()