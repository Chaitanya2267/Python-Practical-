# 1. Read contents from a file and display on console

# f = open("sample.txt", "w")
# f.write("hello python!\n")
# f.write("this is file handling program")
# f.close()

# f = open("sample.txt", "r")
# data = f.read()

# print("file contents:")
# print(data)

# f.close()

with open("sample.txt", "w") as f:
    f.write("hello python!\n")
    f.write("this is file handling program using with keyword")

with open("sample.txt", "r") as f:
    data = f.read()
print("file contents:")
print(data)