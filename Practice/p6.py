# file = open("student.txt", "w")
# file.write("Name: csw\n")
# file.write("Course: B.Tech\n")
# file.write("Subject: Python\n")
# file.close()
# print("Data written successfully.")

# file = open("student.txt", "r")
# data = file.read()
# print(data)
# file.close()

# file = open("student.txt", "a")
# file.write("\nSemester: 5\n")
# file.close()
# print("done")

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)

# with open("student.txt", "r") as file:
#     lines = file.readlines()
# print("total lines: ",len(lines))

# try:
#     with open("unknown.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Error: file does not exist")

import os
# os.mkdir("PythonFiles")
# print("Done")

# if os.path.exists("PythonFiles"):
    # print("exist")
# else:
    # print("does not exist")

# items = os.listdir(".")
# for item in items:
#     print(item)

# os.rename("PythonFiles", "studentfiles")