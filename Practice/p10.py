import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 30, 25]

# plt.plot(x, y, marker='o')
# plt.title("Line Graph")
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.grid(True)
# plt.show()



subjects = ["Python", "Java", "Cloud", "DSA"]
marks = [85, 75, 90, 80]

# plt.bar(subjects, marks)
# plt.title("Marks by Subject")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.show()

plt.barh(subjects, marks)
plt.title("Marks by Subject")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()



# labels = ["Python", "Java", "Cloud", "DSA"]
# values = [30, 25, 20, 25]

# plt.pie(values, labels=labels, autopct='%1.1f%%')
# plt.title("Study Time Distribution")
# plt.show()




# x = [1, 2, 3, 4, 5]
# y = [2, 4, 3, 7, 6]

# plt.scatter(x, y)
# plt.title("Scatter Plot")
# plt.xlabel("X values")
# plt.ylabel("Y values")
# plt.show()




# marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80]

# plt.hist(marks, bins=5, edgecolor='black')
# plt.title("Distribution of Marks")
# plt.xlabel("Marks")
# plt.ylabel("Frequency")
# plt.show()