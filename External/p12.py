class Father:
    def show1(self):
        print("Father class")

class Mother:
    def show2(self):
        print("Mother class")

class Child(Father, Mother):
    def show3(self):
        print("Child class")

obj = Child()

obj.show1()
obj.show2()
obj.show3()