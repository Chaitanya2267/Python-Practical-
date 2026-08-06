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

# password = input("Enter password: ")
# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False
# if len(password) < 8:
#     print("Invalid Password")
# else:
#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_digit = True
#         else:
#             has_special = True
#     if has_upper and has_lower and has_digit and has_special:
#         print("Valid Password")
#     else:
#         print("Invalid Password")

# --------------------------------------------------------------------------------------------------
# 22. Run-Length Encoding
# Compress a string by counting consecutive repeated characters.
# Example: Input: aaabbccccd Output: a3b2c4d1

# text = input("Enter a string: ")
# count = 1
# for i in range(len(text) - 1):
#     if text[i] == text[i+1]:
#         count += 1
#     else:
#         print(text[i] + str(count), end="")
#         count = 1
# print(text[-1] + str(count))

# --------------------------------------------------------------------------------------------------
# 23. String Compression  
# Compress repeated characters and return the original string if compression does not reduce the length.

# text = input("Entr a string: ")
# compressed = ""
# count = 1
# for i in range(len(text) - 1):
#     if text[i] == text[i + 1]:
#         count += 1
#     else:
#         compressed += text[i] + str(count)
#         count = 1
# compressed += text[-1] + str(count)
# if len(compressed) < len(text):
#     print("Compressed String:", compressed)
# else:
#     print("Original String:", text)

# --------------------------------------------------------------------------------------------------
# 24. Most Frequent Character  
# Find the character with the highest frequency.

# text = input("Enter a string: ")
# printed = ""
# max_count = 0
# max_char = ""
# for ch in text:
#     if ch not in printed:
#         count = 0
#         for c in text:
#             if ch == c:
#                 count += 1
#         if count > max_count:
#             max_count = count
#             max_char = ch
#         printed += ch
# print("Most Frequent Character:", max_char)
# print("Frequency:", max_count)

# text = input("Enter a string: ")
# freq = {}
# for ch in text:
#     freq[ch] = freq.get(ch, 0) + 1
# max_char = ""
# max_count = 0
# for ch in freq:
#     if freq[ch] > max_count:
#         max_count = freq[ch]
#         max_char = ch
# print("Enter Frequent Character:", max_char)
# print("Frequency:", max_count)

# --------------------------------------------------------------------------------------------------
# 25. Second Most Frequent Character  
# Find the second most frequently occurring character.

# text = input("Enter a string: ")
# printed =""
# first_count = 0
# first_char = ""
# second_count = 0
# second_char = ""
# for ch in text:
#     if ch not in printed:
#         count = 0
#         for c in text:
#             if ch == c:
#                 count += 1
#         if count > first_count:
#             second_count = first_count
#             second_char = first_char
#             first_count = count
#             first_char = ch
#         elif count > second_count:
#             second_count = count
#             second_char = ch
#         printed += ch
# print("Most Frequent Character: ", first_char)
# print("Second Most Frequent: ", second_char)
# print("Frequency: ", second_count)

# --------------------------------------------------------------------------------------------------
# 26. Caesar Cipher  
# Encrypt and decrypt a message using the Caesar Cipher algorithm.

# Encryption Program

# message = input("Enter message:")
# shift = int(input("Enter shift: "))
# encrypted = ""
# for ch in message:
#     if ch.isupper():
#         encrypted += chr((ord(ch) - 65 + shift) % 26 + 65)
#     elif ch.islower():
#         encrypted += chr((ord(ch) - 97 + shift) % 26 + 97)
#     else:
#         encrypted += ch
# print("Encrypted Mesage:", encrypted)

# Decryption Program

# message = input("Enter encrypted message: ")
# shift = int(input("Enter shift: "))
# decrypted = ""
# for ch in message:
#     if ch.isupper():
#         decrypted += chr((ord(ch) - 65 - shift) % 26 + 65)
#     elif ch.islower():
#         decrypted += chr((ord(ch) - 97 - shift) % 26 + 97)
#     else:
#         decrypted += ch
# print("Decrypted message: ", decrypted)

# --------------------------------------------------------------------------------------------------
# 27. Email Validator  
# Validate whether a given email address follows a valid format. 

# email = input("Enter email: ")
# if email.count("@") != 1:
#     print("Invalid Email")
# else:
#     parts = email.split("@")
#     username = parts[0]
#     domain = parts[1]
#     if username == "":
#         print("Invalid Email")
#     elif domain == "":
#         print("Invalis Email")
#     elif "." not in domain:
#         print("Invalis Email")
#     else:
#         print("Valid Email")

# import re
# email = input("Enter email: ")
# pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
# if re.match(pattern, email):
#     print("Valid Email")
# else:
#     print("Invalid Email")

# --------------------------------------------------------------------------------------------------
# 28. Word Frequency Dictionary  
# Count the frequency of every word in a paragraph.

# paragraph = input("Enter a paragraph: ")
# words = paragraph.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print("Word Frequencies")
# for word in freq:
#     print(word, ":", freq[word])

# --------------------------------------------------------------------------------------------------
# 29. Sentence Reversal  
# Reverse the order of words in a sentence without changing the words themselves.   

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# for i in range(len(words)-1, -1, -1):
#     print(words[i], end=" ")

# sentence = input("Enter a sentence: ")
# words = sentence.split()
# print(" ".join(words[::-1]))

# --------------------------------------------------------------------------------------------------
# 30. String Rotation  
# Check whether one string is a rotation of another.

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if len(s1) != len(s2):
#     print("No")
# else:
#     temp = s1 + s2
#     if s2 in temp:
#         print("Yes")
#     else:
#         print("No")

# --------------------------------------------------------------------------------------------------
