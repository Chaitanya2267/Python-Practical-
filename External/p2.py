# 2. Read contents from one file and write into another file

# f = open("source.txt", "w")
# f.write("welcome to python")
# f.close()

# f = open("source.txt", "r")
# data = f.read()
# f.close()

# f = open("destination.txt", "w")
# f.write(data)
# f.close()

# print("contents copied successfully")

# f = open("destination.txt", "r")
# print(f.read())
# f.close()

with open("source.txt", "w") as f:
    f.write("welcome to python")

with open("source.txt", "r") as f:
    data = f.read()

with open("destination.txt", "w") as f:
    f.write(data)

with open("destination.txt", "r") as f:
    print(f.read())