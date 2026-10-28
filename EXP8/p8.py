# # Polymorphism through method overriding
# class Animal:
# 	def sound(self):
# 		return "Animal makes a sound"


# class Dog(Animal):
# 	def sound(self):
# 		return "Dog barks"


# class Cat(Animal):
# 	def sound(self):
# 		return "Cat meows"


# print("Method overriding")
# animals = [Dog(), Cat()]
# for animal in animals:
# 	print(animal.sound())


# # Program 2: Polymorphism through duck typing
# class Car:
# 	def move(self):
# 		return "Car is driving"


# class Boat:
# 	def move(self):
# 		return "Boat is sailing"


# def start_moving(vehicle):
# 	print(vehicle.move())


# print("\nDuck typing")
# start_moving(Car())
# start_moving(Boat())


# # Program 3: Polymorphism through operator overloading
# class Addition:
#     def __init__(self, a):
#         self.a = a

#     def __add__(self, other):
#         return self.a + other.a


# obj1 = Addition(10)
# obj2 = Addition(20)

# print("Addition:", obj1 + obj2)
