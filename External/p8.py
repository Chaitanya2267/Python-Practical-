# method overloading
# Defining methods that perform similar operations with different numbers of arguments.

class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calculator()

print("addition of 1 number:", obj.add(10))
print("addotion of 2 number:", obj.add(10, 20))
print("addition of 3 number:", obj.add(10, 20, 30))