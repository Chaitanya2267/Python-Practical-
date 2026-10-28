# Write a program to input a string and display its length without using the len() function
# str =input(str("Enter a string:"))
# print(str,len(str))


# 2.	Character Count 
# ●	Count the number of vowels, consonants, digits, spaces, and special characters in a given string.

# s = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# vowel_count = 0
# consonant_count = 0
# digit_count = 0
# space_count = 0
# special_count = 0

# for ch in s:
#     if ch.isalpha():
#         if ch in vowels:
#             vowel_count += 1
#         else:
#             consonant_count += 1
#     elif ch.isdigit():
#         digit_count += 1
#     elif ch.isspace():
#         space_count += 1
#     else:
#         special_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)
# print("Digits:", digit_count)
# print("Spaces:", space_count)
# print("Special characters:", special_count)





# # 3.	Reverse a String 
# # ●	Reverse the given string without using built-in reverse functions. 
# str = "Python"
# print(str[::-1])


# Palindrome Check 
# ●	Check whether the entered string is a palindrome
# str=input(str("Enter the string:"))
# rev=str[::-1]
# if str==rev:
#     print("Its palindrome")
# else:
#     print("Its not palindrome")




# 5.	Uppercase and Lowercase Count 
# ●	Count the number of uppercase and lowercase letters in a string. 

# str = input("Enter the string: ")
# u_count = 0
# l_count = 0

# for char in str:
#     if char.isupper():
#         u_count += 1
#     elif char.islower():
#         l_count += 1

# print("Number of uppercase letters:", u_count)
# print("Number of lowercase letters:", l_count)



# 6.	Replace Characters 
# ●	Replace all occurrences of a given character with another character. 
# Input data
# text = "banana"
# old= "a"
# new = "o"

# result = text.replace(old, new)
# print(result)


# Remove Spaces 
# ●	Remove all spaces from the input string. 

# text = "P y th o n"
# space_remove= text.replace(" ", "")
# print(space_remove)  



# 8.Frequency of a Character 
# ●	Find the number of times a specified character appears in a string. 
# text = "banana"
# freq = {}

# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1

# print(freq)


# First and Last Character 
# ●	Print the first and last character of a string. 




# First and Last Character 
# ●	Print the first and last character of a string. 
# text="hello"
# print(text[0])
# print(text[-1])



# Define the input string
# text = "Hello!"

# for char in text:
#     print(f"Character: {char} -> ASCII Value: {ord(char)}")


# 11.	Word Count 
# a.	Count the total number of words in a sentence. 
# text="Python is fun"
# words=text.split()
# print(words)
# count=0
# if " ":
#         count=len(words)
# print("Total no of words:",count)



# 12.	Longest Word 
# a.	Find the longest word in a given sentence.

# text="Python is a programming language"
# words = text.split()
# longest = ""


# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest word:", longest)
# print("Length:", len(longest))



# 13.	Shortest Word 
# a.	Find the shortest word in a sentence. 

# text = "Python is a programming language"
# words = text.split()
# shortest = words[0]   

# for word in words:
#     if len(word) < len(shortest):
#         shortest = word

# print("Shortest word:", shortest)
# print("Length:", len(shortest))



# 14.	Title Case 
# a.	Convert the first letter of every word to uppercase. 
# text="i am happy today"
# print(text.title())

# 15.	Duplicate Characters 
# a.	Print all duplicate characters in a string. 
# text = "aabewwmmc"
# seen = []

# for ch in text:
#     if ch not in seen:
#         if text.count(ch) > 1:
#             print(ch)
#         seen.append(ch)


# 16.	Character Frequency 
# a.	Display the frequency of every character in a string. 



# 17.	Anagram Check 
# a.	Check whether two strings are anagrams. 
# text1="One"
# text2="Two"
# if sorted(text1.lower()) == sorted(text2.lower()):
#     print("Its anagram")
# else:
#     print("Its not anagram")


# 18.	Remove Duplicate Characters 
# a.	Remove duplicate characters while maintaining the original order. 
# text = "aabewwmmc"
# result = ""

# for ch in text:
#     if ch not in result:
#         result += ch

# print("After removing duplicates:", result)



# 19. Substring Search
# a. Check whether a given substring exists in the main string.

# text = "Python is easy"
# sub = "easy"

# if sub in text:
#     print("Substring found")
# else:
#     print("Substring not found")
    
    
# 20. Count Occurrences of a Word
# a. Count how many times a specific word appears in a sentence.

# text = "Python is easy and Python is powerful"
# word = "Python"
# count = text.split().count(word)
# print("Occurrences:", count)


# 21. Password Validator
# a. Validate a password based on these conditions:
#    - Minimum 8 characters
#    - At least one uppercase letter
#    - One lowercase letter
#    - One digit
#    - One special character

# password = input(str("Enter the password"))

# upper = lower = digit = special = False

# for ch in password:
#     if ch.isupper():
#         upper = True
#     elif ch.islower():
#         lower = True
#     elif ch.isdigit():
#         digit = True
#     else:
#         special = True

# if len(password) >= 8 and upper and lower and digit and special:
#     print("Valid Password")
# else:
#     print("Invalid Password")


# 22.	Run-Length Encoding
# ●	Compress a string by counting consecutive repeated characters. 
# ●	Example:
# 	Input: aaabbccccd
# 	Output: a3b2c4d1

s = "aaabbccccd"
result = ""
count = 1

for ch in range(1,len(s)):
    if s[ch]==s[ch-1]:
        count+=1
    else:
        result+=s[ch-1]+str(count)
        count=1
result+=s[-1]+str(count)

print(result)








