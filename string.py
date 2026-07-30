# 2.
# name='ved'
# print(name)
# print(len(name))

# city="Kolhapur"
# print(city)
# print(len(city))

# Message="""Python is programming language.
# It used in web development.
#         """
# print(Message)
# print(len(Message))

# 3.
# Greet="welcome to everyone."
# result1 = Greet.capitalize()
# print(result1)

# 4.
# text = "python is FUN!"
# result2 = text.upper()
# print(result2) 

# text = "python is FUN!"
# result2 = text.upper()
# print(result2) 

# 5.
# text2 = "Python"
# result3 = text2.endswith(input("enter a char: "))
# print(result3)

# text2 = input("enter a string: ")
# result3 = text2.startswith("P")
# print(result3)

# 6.
# text = "Python"
# reversed_text = text[::-1]
# print(reversed_text)  

# s = input("enter a string: ")
# reversed_text = s[::-1]
# print(reversed_text)

# 7.
# m = "madam"
# is_palindrome = m == m[::-1]
# print(is_palindrome)  

# o = input("enter a string: ")
# is_palindrome = o == o[::-1]
# print(is_palindrome)

# 8.
# s = input("Enter a string: ")
# print("First characte", s[0])
# print("Last characte", s[-1])

# s = "sahil"
# print("First characte", s[0])
# print("Last characte", s[-1])

# 9.
from collections import Counter

text = "madam"
frequencies = Counter(text)
print(dict(frequencies))  
