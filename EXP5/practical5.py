# f = open("data.txt", "r")
# content = f.read()
# print(content)
# f.close()  

# f = open("data.txt", "w")   
# f.write("Hello, this is a test.\n")
# f.write("Second line here.")
# f.close()

# f = open("data.txt", "a")  
# f.write("\nThis line is appended.")
# f.close()

# f = open("data.txt", "r")
# line = f.readline()
# print(line)
# f.close()

# f = open("data.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()


# f = open("data.txt", "w")
# lines = ["First line\n", "Second line\n", "Third line\n"]
# f.writelines(lines)
# f.close()

# f = open("data.txt", "r+")
# print(f.read())
# f.write("\nNew line")
# f.close()

# f = open("data.txt", "w+")
# f.write("Fresh start\n")
# f.seek(0)
# print(f.read())
# f.close()

# f = open("data.txt", "a+")
# f.write("\nAppended line")
# f.seek(0)
# print(f.read())
# f.close()

# f = open("data.txt", "rb")
# content = f.read()
# print("\nFile content", content)
# f.close()

# f = open("output.bin", "rb+")
# content = f.read()
# f.seek(0)
# print(f.read())
# f.close()

# f = open("output.bin", "wb")
# f.write(b"Hello in binary")
# f.close()

# f = open("output.bin", "ab")
# f.write(b"\nAppended binary data")
# f.close()

# f = open("output.bin", "rb")
# content = f.read()
# print("\nFile content", content)
# f.close()

# with open("data.txt", "wb") as file:
#     print("This is statement using wiht keyword.")

