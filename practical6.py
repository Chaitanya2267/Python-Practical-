# 1. lambda function
# print("Normal Function:")
# def add(a, b):
#     return a + b
# print("Addition:", add(20, 30))

# print("Function with default arguments:")
# def greet(name="csw"):
#     print("Hello", name)
# greet()
# greet("tanmay")

# print("Lambda Function:")
# square = lambda x: x*x
# n = int(input("Enter a number to find its square: "))
# print(f"Square of {n}: {square(n)}")

# print("lambda function with 2 arguments:")
# multiply = lambda x, y: x *y
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# print(f"Multiplication of {x} and {y}: {multiply(x, y)}")

# 2. module

# import module
# print("Addition:", module.add(20, 30))  
# print("Subtraction:", module.subtract(50, 20))  
# print("Multiplication:", module.multiply(5, 6)) 
# print("Division:", module.divide(10, 2))

# 3. array

# from array import array
# num = array('i', [1,2,3,4,5])
# print("Array elements:", num)

from array import array
num = array('i', [1, 2, 3, 4, 5])
print( *num)