import re

text = "Hello 123 World 456"

# 1. findall() → Extract all numbers
numbers = re.findall(r'\d+', text)
print("Numbers:", numbers)

# 2. split() → Split text at digits
parts = re.split(r'\d+', text)
print("Split result:", parts)

# 3. sub() → Replace digits with '#'
new_text = re.sub(r'\d+', '#', text)
print("Sub result:", new_text)

# 4. search() → Find first number
match = re.search(r'\d+', text)
if match:
    print("First number found:", match.group())

# 5. escape() → Treat special characters literally
special_text = "Hello (Python)*+?"
pattern = re.escape(special_text)
print("Escaped pattern:", pattern)

match2 = re.search(pattern, "I love Hello (Python)*+? regex")
print("Match found:", match2.group())

# 6. compile() → Reusable regex object
pattern_obj = re.compile(r'\d+')

text1 = "Order number 789"
text2 = "Invoice 456"

print("Numbers in text1:", pattern_obj.findall(text1))
print("Numbers in text2:", pattern_obj.findall(text2))
