import matplotlib.pyplot as plt 

subjects = ['python', 'java', 'c++', 'PHP']
marks = [40, 30, 20, 10]

plt.pie(marks, labels = subjects, autopct='%1.1f%%')
plt.title("subjects distribution")
plt.show()