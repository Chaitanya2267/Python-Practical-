# Program to create a file and write student details

# Open the file in write mode
f = open("student.txt", "w")

# Student details
name = "CSW"
roll_no = "13"
branch = "Computer Science"
semester = "5th"

# Writing details into the file
f.write("Name: " + name + "\n")
f.write("Roll Number: " + roll_no + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + semester + "\n")

# Close the file
f.close()

print("Student details written successfully to student.txt")


# Program to open a text file and display its contents

# Open the file in read mode
f = open("student.txt", "r")

# Read the entire file
content = f.read()

# Display the contents
print("File Contents:\n")
print(content)

# Close the file
f.close()

# Program to append student information to an existing file

# Open the file in append mode
f = open("student.txt", "a")

# Additional student details
name = "Rahul"
roll_no = "12"
branch = "Information Technology"
semester = "3rd Year"

# Writing details into the file
f.write("\nName: " + name + "\n")
f.write("Roll Number: " + roll_no + "\n")
f.write("Branch: " + branch + "\n")
f.write("Semester: " + semester + "\n")

# Close the file
f.close()

print("Additional student details appended successfully to student.txt")

# Program to read a text file line by line

# Open the file in read mode
f = open("student.txt", "r")

# Read and display each line
print("File Contents (line by line):\n")
for line in f:
    print(line.strip())   # strip() removes extra newline characters

# Close the file
f.close()


# Program to count total number of lines in a text file

# Open the file in read mode
f = open("student.txt", "r")

# Initialize line counter
line_count = 0

# Count lines one by one
for line in f:
    line_count += 1

# Display the total number of lines
print("Total number of lines in student.txt:", line_count)

# Close the file
f.close()

# Program to count total number of words in a text file

# Open the file in read mode
f = open("student.txt", "r")

# Read the entire file
content = f.read()

# Split content into words
words = content.split()

# Count the words
word_count = len(words)

# Display the total number of words
print("Total number of words in student.txt:", word_count)

# Close the file
f.close()
