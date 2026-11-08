import matplotlib.pyplot as plt 

languages = ['java', 'python', 'PHP', 
             'javascript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(languages, popularity)

plt.xlabel("popularity")
plt.ylabel("programming languages")
plt.title("popularity of programming languages")

plt.show()