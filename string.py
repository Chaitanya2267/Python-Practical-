# 1. String Length 
 
# text = input("Enter a string: ")
# count = 0;
# for i in text:
#     count += 1
# print(count)

# --------------------------------------------------------------------------------------------------
# 2. Character Count  

# text = input("Enter a string: ")
# vowels = 0
# consonants = 0
# digits = 0
# spaces = 0
# special = 0

# for ch in text:
#     if ch.isalpha():
#         if ch in "aeiouAEIOU":
#             vowels += 1
#         else:
#             consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# print("Vowels = ", vowels)
# print("Consonants = ", consonants)
# print("Digits = ", digits)
# print("Spaces = ", spaces)
# print("Special Characters = ", special)

# --------------------------------------------------------------------------------------------------
# 3. Reverse a String

# text = input("Enter a string: ")
# reverse = ""
# for i in range( len(text) - 1, -1, -1 ):
#     reverse += text[i]
# print("Reversed string: ", reverse)

# text = input("Enter a string: ")
# print(text[::-1])

# --------------------------------------------------------------------------------------------------
# 4. Palindrome Check

# text = input("Enter a string: ")
# reverse = ""
# for i in range ( len(text) - 1, -1, -1 ):
#     reverse += text[i]
# if text == reverse:
#     print("Palindrom")
# else:
#     print("Not a palindrome.")

# text = input("Enter a string: ")
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# --------------------------------------------------------------------------------------------------
# 5. Uppercase and Lowercase Count

# text = input("Enter a string: ")
# uppercase = 0
# lowercase = 0
# for ch in text:
#     if ch.isupper():
#         uppercase += 1
#     elif ch.islower():
#         lowercase += 1
# print("Uppercase: ", uppercase)
# print("Lowercase: ", lowercase)

# if 'A' <= ch <= 'Z': uppercase += 1
# elif 'a' <= ch <= 'z': lowercase += 1

# --------------------------------------------------------------------------------------------------
# 6. Replace Characters  

# text = input("Enter a string: ")
# org = input("Enter character to replace: ")
# new = input("Enter new character: ")
# result = ""
# for ch in text:
#     if ch == org:
#         result += new
#     else:
#         result += ch
# print("New string: ", result)

# --------------------------------------------------------------------------------------------------
# 7. Remove Spaces  

# text = input("Enter a string: ")
# result = ""
# for ch in text:
#     if ch != " ":
#         result += ch
# print("String without space:",result)

# text = input("Enter a string: ")
# print(text.replace(" ", ""))

# --------------------------------------------------------------------------------------------------
# 8. Frequency of a Character
# text = input("Enter a string: ")
# target = input("Enter a character: ")
# count = 0
# for ch in text:
#     if ch == target:
#         count += 1
# print("Frequency =", count)

# --------------------------------------------------------------------------------------------------
# 9. First and Last Character
text = input("Enter a string: ")  
if text == " ":
    print("The string is empty.")
else:
    print("First character: ", text[0])
    print("Last character: ", text[-1])
# print("Last character: ", text[len(text) - 1])

# --------------------------------------------------------------------------------------------------
# 10. 

# --------------------------------------------------------------------------------------------------