
# Integer
age = 20
print("Integer:", age)
print(type(age))

# Float
height = 5.8
print("\nFloat:", height)
print(type(height))

# Complex
num = 3 + 4j
print("\nComplex:", num)
print(type(num))

# String
name = "Viraj"
print("\nString:", name)
print(type(name))

# Boolean
is_student = True
print("\nBoolean:", is_student)
print(type(is_student))

# List (Mutable)
marks = [85, 90, 95]
print("\nList:", marks)
print(type(marks))

# Tuple (Immutable)
colors = ("Red", "Green", "Blue")
print("\nTuple:", colors)
print(type(colors))

# Set (Unique values)
numbers = {10, 20, 30, 20}
print("\nSet:", numbers)
print(type(numbers))

# Dictionary (Key-Value)
student = {
    "Name": "Viraj",
    "Age": 20,
    "Branch": "CSE"
}
print("\nDictionary:", student)
print(type(student))

# None Type
value = None
print("\nNone:", value)
print(type(value))

# int -> float
a = 10
print("\nInt to Float:", float(a))

# float -> int
b = 15.9
print("Float to Int:", int(b))

# int -> str
c = 100
print("Int to String:", str(c))

# str -> int
d = "200"
print("String to Int:", int(d))

# bool -> int
e = True
print("Bool to Int:", int(e))

# int -> bool
f = 0
print("Int to Bool:", bool(f))

marks[0] = 99
print("\nUpdated List:", marks)
