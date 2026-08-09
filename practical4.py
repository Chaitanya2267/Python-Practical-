# 1. simple student grade management system

# students = []
# grades = []

# def add_student():
#     name = input("Enter student name: ")
#     grade = float(input("Enter grade: "))
#     students.append(name)
#     grades.append(grade)
#     print("student added successfully.")

# def update_grade():
#     name = input("Enter student name: ")
#     if name in students:
#         index = students.index(name)
#         grades[index] = float(input('Enter new grade: '))
#         print("Grade updated")
#     else:
#         print("Student not found")

# def remove_student():
#     name = input("Enter Student name: ")
#     if name in students:
#         index = students.index(name)
#         students.pop(index)
#         grades.pop(index)
#         print("Student removed")
#     else:
#         print("Student not found")

# def average_grade():
#     if len(grades) > 0:
#         print("average_grade =", sum(grades) / len(grades))
#     else:
#         print("No student record")

# def display_extremes():
#     if len(grades) > 0:
#         print("Highest grade =", max(grades))
#         print("Lowest grade =", min(grades))
#     else:
#         print("No student record")

# def display_students():
#     if len(students) == 0:
#         print("No student")
#     else:
#         print("\nStudent List")
#         for i in range(len(students)):
#             print(students[i], "-", grades[i])
        
# while True:
#     print("\nStudent Grade Management System")
#     print("1. Add Student")
#     print("2. Update Grade")
#     print("3. Remove Student")
#     print("4. Average Grade ")
#     print("5. Highest & Lowest Grade")
#     print("6. Display students")
#     print("7. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         add_student()

#     elif choice == 2:
#         update_grade()

#     elif choice == 3:
#         remove_student()

#     elif choice == 4:
#         average_grade()

#     elif choice == 5:
#         display_extremes()

#     elif choice == 6:
#         display_students()

#     elif choice == 7:
#         print("Program Ended")
#         break

#     else:
#         print("Invalid choice")

# --------------------------------------------------------------------------------------------------

# 2. a system that manages the positions of points in a 2D plane.

# import math

# def distance(p1, p2):
#     x1 = p1[0]
#     y1 = p1[1]

#     x2 = p2[0]
#     y2 = p2[1]

#     d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return d

# def farthest_points(points):
#     farthest = points[0]
#     max_distance = math.sqrt(points[0][0]**2 + points[0][1]**2)

#     for point in points:
#         current = math.sqrt(point[0]**2 + point[1]**2)

#         if current > max_distance:
#             max_distance = current
#             farthest = point

#     return farthest

# points = []

# n = int(input("Enter number of points: "))

# for i in range(n):

#     x = int(input("Enter x coordinate: "))
#     y = int(input("Enter y coordinate: "))
#     points.append((x, y))

# print("\nPoints: ", points)

# i = int(input("Enter first point index: "))
# j = int(input("Enter second points index: "))

# print("Distance=", distance(points[i], points[j]))
# print("Farthest Point=", farthest_points(points))

# --------------------------------------------------------------------------------------------------
# 3. a configuration system for a web server

# server_ip = ("192.168.1.10",)

# allowed_ips = [
#     "192.168.1.5",
#     "192.168.1.6"
# ]

# def update_allowed_ips():
#     print("\n1. Add IP")
#     print("2. Remove IP")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         ip = input("Enter IP to add: ")
#         allowed_ips.append(ip)
#         print("IP added successfully")

#     elif choice == 2:
#         ip = input("Enter IP to remove: ")
#         if ip in allowed_ips:
#             allowed_ips.remove(ip)
#             print("IP removed successfully")
#         else:
#             print("IP not found")

#     else:
#         print("Invalid choice")

# def display_configuration():
#     print("\nServer configuration")
#     print("Server IP: ", server_ip)
#     print("Allowed IPs: ", allowed_ips)

# while True:
#     print("\n1. Update Allowed IPs")
#     print("2. Display configuration")
#     print("3. Exit")

#     if choice == 1:
#         update_allowed_ips()

#     elif choice == 2:
#         display_configuration()

#     elif choice == 3:
#         print("Program ended.")
#         break

#     else:
#         print("Invalid choice")

# --------------------------------------------------------------------------------------------------
# 4. manage two different projects in your company

# project_a = set(input("Enter Employees of Project A:").split())
# project_b = set(input("Enter Employees of Project B:").split())

# all_employees = project_a.union(project_b)
# both_projects = project_a.intersection(project_b)
# only_project_a = project_a - project_b
# only_project_b = project_b - project_a

# print("Total unique Employees:", all_employees)
# print("Employees in both projects:", both_projects)
# print("Employees only in Project A:", only_project_a)
# print("Employees only in Project B:", only_project_b)

# --------------------------------------------------------------------------------------------------
# 5. build a simple text analysis tool

# import string
# text = input("Enter a paragraph: ")
# text = text.translate(str.maketrans("", "", string.punctuation))
# words = text.split()
# print("Total number of words: ", len(words))

# frequency = {}
# for word in words:
#     word = word.lower()
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1
# print("\nWord frequency:")

# for word, count in frequency.items():
#     print(word, ":", count)

# sorted_words = sorted(
#     frequency.items(),
#     key=lambda x:x[1],
#     reverse=True
# )

# print("\nTop 3 most frequency wprds:")
# for word, count in sorted_words[:3]:
#     print(word, ":", count)

# vowels = "aeiou"
# vowel_count = 0
# for char in text.lower():
#     if char in vowels:
#         vowel_count += 1
# print("\nNumber of vowels:", vowel_count)

# --------------------------------------------------------------------------------------------------
