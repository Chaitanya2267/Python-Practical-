# 1. String Length 
# Write a program to input a string and display its length without using the len() function.  

# text = input("Enter a string: ")
# count = 0;
# for i in text:
#     count += 1
# print(count)

# --------------------------------------------------------------------------------------------------
# 2. Character Count  
# Count the number of vowels, consonants, digits, spaces, and special characters in a given string.

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
# Reverse the given string without using built-in reverse functions. 

# text = input("Enter a string: ")
# reverse = ""
# for i in range( len(text) - 1, -1, -1 ):
#     reverse += text[i]
# print("Reversed string: ", reverse)

# text = input("Enter a string: ")
# print(text[::-1])

# --------------------------------------------------------------------------------------------------
# 4. Palindrome Check
# Check whether the entered string is a palindrome.  

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
# Count the number of uppercase and lowercase letters in a string.  

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
# Replace all occurrences of a given character with another character.  

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
# Remove all spaces from the input string.  

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
# Find the number of times a specified character appears in a string. 

# text = input("Enter a string: ")
# target = input("Enter a character: ")
# count = 0
# for ch in text:
#     if ch == target:
#         count += 1
# print("Frequency =", count)

# --------------------------------------------------------------------------------------------------
# 9. First and Last Character
# Print the first and last character of a string.  

# text = input("Enter a string: ")  
# if text == " ":
#     print("The string is empty.")
# else:
#     print("First character: ", text[0])
#     print("Last character: ", text[-1])
# print("Last character: ", text[len(text) - 1])

# --------------------------------------------------------------------------------------------------
# 10. ASCII Values 
# Display each character of a string along with its ASCII value.

# text = input("Enter a string: ")
# for ch in text:
#     print(ch, "-->", ord(ch))

# --------------------------------------------------------------------------------------------------
# 11. Word Count 
# Count the total number of words in a sentence.  

# text = input("Enter a String: ")
# count = 1
# for ch in text:
#     if ch == " ":
#         count += 1
# print("Number of words: ", count)

# --------------------------------------------------------------------------------------------------
# 12. Longest Word  
# Find the longest word in a given sentence. 

# text = input("Enter a String: ")
# words = text.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word: ", longest)

# --------------------------------------------------------------------------------------------------
# 13. Shortest Word
# Find the shortest word in a sentence. 

# text = input("Enter a string: ")
# words = text.split()
# shortest = words[0]
# for word in words:
#     if len(word) < len(shortest):
#         shortest = word
# print("Shortest word: ", shortest)

# --------------------------------------------------------------------------------------------------
# 14. Title Case  
# Convert the first letter of every word to uppercase. 

# text = input("Enter a string: ")
# print("Title case: ", text.title())

# text = input("Enter a string: ")
# result = ""
# for i in range(len(text)):
#     if i == 0 or text[i-1] == " ":
#         result += text[i].upper()
#     else:
#         result += text[i]
# print("Title Case: ", result)

# --------------------------------------------------------------------------------------------------
# 15. Duplicate Characters  
# Print all duplicate characters in a string.  

# text = input("Enter a string: ")
# printed = ""
# for ch in text:
#     if ch not in printed:
#         count = 0
#         for c in text:
#             if ch == c:
#                 count += 1
#         if count > 1:
#             print(ch)
#             printed += ch

# text = input("Enter a string: ")
# freq = {}
# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1
# for ch in freq:
#     if freq[ch] > 1:
#         print(ch)

# --------------------------------------------------------------------------------------------------
# 16. Character Frequency  
# Display the frequency of every character in a string.

# text = input("Enter a string: ")
# printed = ""
# for ch in text:
#     if ch not in printed:
#         count = 0
#         for c in text:
#             if ch == c:
#                 count += 1
#         print(ch, "-->", count)
#         printed += ch 

# text = input("Enter a string: ")
# freq = {}
# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1
# for ch in freq:
#     print(ch, "-->", freq[ch])

# --------------------------------------------------------------------------------------------------
# 17. Anagram Check  
# Check whether two strings are anagrams. 

# text1 = input("Enter a string: ")
# text2 = input("Enter a string: ")
# if sorted(text1) == sorted(text2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")

# text1 = input("Enter a string: ")
# text2 = input("Enter a string: ")
# if len(text1) != len(text2):
#     print("Not Anagrams")
# else:
#     flag = True
#     for ch in text1:
#         if text1.count(ch) != text2.count(ch):
#             flag = False
#             break
#     if flag:
#             print("Anagrams")
#     else:
#             print("Not Anagrams")

# --------------------------------------------------------------------------------------------------
# 18. Remove Duplicate Characters
# Remove duplicate characters while maintaining the original order. 

# text = input("Enter a string: ")
# result = ""
# for ch in text:
#     if ch not in result:
#         result += ch
# print("After removing duplicates: ",result)

# --------------------------------------------------------------------------------------------------
# 19. Substring Search  
# Check whether a given substring exists in the main string. 

# main = input("Enter the main string: ").lower()
# sub = input("Enter the substring: ").lower()
# if sub in main:
#     print("Substring found")
# else:
#     print("Substring not found")

# --------------------------------------------------------------------------------------------------
# 20. Count Occurrences of a Word
# Count how many times a specific word appears in a sentence. 

# sentence = input("Enter a sentence: ").lower()
# target = input("Enter the word to search: ").lower()
# words = sentence.split()
# count = 0
# for word in words:
#     if word == target:
#         count += 1
# print("Occurrences =", count)

# sentence = input("Enter a sentence: ").lower()
# target = input("Enter the word: ").lower()
# words = sentence.split()
# print("Occurrences =", words.count(target))

# --------------------------------------------------------------------------------------------------
# 21. Password Validator 
# Validate a password based on these conditions:  
# Minimum 8 characters, At least one uppercase letter, One lowercase letter, One digit, One special character 

