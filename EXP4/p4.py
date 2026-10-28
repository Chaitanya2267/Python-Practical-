
# # Reading and Writing in the File

# # 1. Write and Read - w+
# with open("report.txt", "w+") as file:
#     print("Writing in the file")

#     while True:
#         line = input("Enter a sentence: ")
#         file.write(line + "\n")

#         choice = input("Do you wish to enter more data? (y/n): ")
#         if choice in ('n', 'N'):
#             break

#     print("The byte position of file object is", file.tell())
#     file.seek(0)

#     print("\nFile contains (Reading from file):")
#     data = file.read()
#     print(data)


# # 2. Read - r
# print("\nRead")
# with open("report.txt", "r") as file:
#     data = file.read()
#     print(data)


# # 3. Write - w
# print("\nWrite")
# with open("report.txt", "w") as file:
#     line = input("Enter text to write: ")
#     file.write(line)


# # 4. Append - a
# print("\nAppend")
# with open("report.txt", "a") as file:
#     line = input("Enter text to append: ")
#     file.write("\n" + line)


# # 5. Read + Write - r+
# print("\nRead + Write")
# with open("report.txt", "r+") as file:
#     line = input("Enter text: ")
#     file.write(line)
#     file.seek(0)
#     data = file.read()
#     print("File content:", data)


# # 6. Write + Read - w+
# print("\nWrite + Read")
# with open("report.txt", "w+") as file:
#     line = input("Enter text: ")
#     file.write(line)
#     file.seek(0)
#     data = file.read()
#     print("File content:", data)


# # 7. Append + Read - a+
# print("\nAppend + Read")
# with open("report.txt", "a+") as file:
#     line = input("Enter text to append: ")
#     file.write("\n" + line)
#     file.seek(0)
#     data = file.read()
#     print("File content:", data)


# # 8. Create New File - x
# print("\nCreate New File")
# try:
#     with open("new_report.txt", "x") as file:
#         file.write("This is a newly created file.")
#         print("new_report.txt created successfully.")
# except FileExistsError:
#     print("new_report.txt already exists.")


# # 9. Read Binary - rb
# print("\nRead Binary")
# with open("report.txt", "rb") as file:
#     data = file.read()
#     print(data)


# # 10. Write Binary - wb
# print("\nWrite Binary")
# with open("binary_report.txt", "wb") as file:
#     data = input("Enter text for binary file: ")
#     file.write(data.encode())


# # 11. Append Binary - ab
# print("\nAppend Binary")
# with open("binary_report.txt", "ab") as file:
#     data = input("Enter text to append to binary file: ")
#     file.write(("\n" + data).encode())


# # 12. tell() and seek()
# print("\ntell() and seek()")
# with open("report.txt", "r") as file:
#     print(file.tell())
#     file.seek(5)
#     print(file.tell())


# # Directory Basic Code
# import os

# # 1. Working Directory
# print("\nWorking Directory")
# print(os.getcwd())


# # 2. List Directory
# print("\nList Directory")
# print(os.listdir())


# # 3. Create Directory
# print("\nCreate Directory")
# if not os.path.exists("myfolder"):
#     os.mkdir("myfolder")
#     print("Directory created")
# else:
#     print("Directory already exists")


# # 4. Rename File
# print("\nRename File")
# os.rename("new1_report.txt", "new_report.txt")


# # 5. Change Path
# print("\nChange Directory")
# os.chdir(r"D:\Sem_V\Training_5")
# print("Current directory:", os.getcwd())


# # 6. Delete Empty Folder
# print("\nDelete Empty Folder")
# os.rmdir("myfolder")
