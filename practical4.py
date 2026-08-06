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
