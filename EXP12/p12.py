
import matplotlib.pyplot as plt

students = ["A", "B", "C", "D", "E"]
marks = [75, 85, 60, 90, 70]

# 1. Line Graph
plt.figure()
plt.plot(students, marks, marker='o')
plt.title("Line Graph")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 2. Bar Chart
plt.figure()
plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# 3. Scatter Plot
# plt.figure()
# plt.scatter(students, marks)
# plt.title("Scatter Plot")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()

# 4. Histogram
# plt.figure()
# plt.hist(marks, bins=5)
# plt.title("Histogram")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()


# 5. Pie Chart
# plt.figure()
# plt.pie(marks, labels=students, autopct='%1.1f%%')
# plt.title("Pie Chart")
# plt.show()
