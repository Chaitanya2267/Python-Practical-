
# If Problems

# 1 check no is zero or non-zero
# Number = int(input("Enter the Number:"))
# if Number!=0:
#     print("Number is Non Zero")
# if Number==0:
#     print("Number is Zero")


# 2 Find largest of two Numbers
# a=int(input("Enter no a:"))
# b=int(input("Enter no b:"))
# if a>b:
#     print(a,"is largest")
# if b>a:
#     print(b,"is largest")


# 3 Check No is +ve or -ve 
# no=float(input("Enter any Number:"))
# if no>0:
#     print(no,"is Positive")
# if no==0:
#     print("Number is zero ")
# if no<0:
#     print(no,"is Negative")


# 4 Check vowel or consonan
# ch = input("Enter a character: ")

# if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
#  or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
#     print(ch, "is a Vowel")
# else:
#     print(ch, "is a Consonant")


# 5 Student Performance 
# sub1 = int(input("Enter Subject 1 marks: "))
# sub2 = int(input("Enter Subject 2 marks: "))
# sub3 = int(input("Enter Subject 3 marks: "))
# sub4 = int(input("Enter Subject 4 marks: "))
# total = sub1 + sub2 + sub3 + sub4
# per = (total / 400) * 100

# print("Total Marks =", total ,"Out of 400")
# print("Percentage =", per)

# if per>=90:
#     print("Excellent Performance")
# elif per>=80:
#     print("Very Good Performance")
# elif per>=70:
#     print("Good Performance")
# elif per>=60:
#     print("Average Performance")
# else:
#     print("Poor Performance")


# 6 Largest of three 
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a > b and a > c:
#     print(a, "is largest")
# elif b > a and b > c:
#     print(b, "is largest")
# else:
#     print(c, "is largest")


# 7 Smallest of three
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))

# if a < b and a < c:
#     print(a, "is Smallest")
# elif b < a and b < c:
#     print(b, "is Smallest")
# else:
#     print(c, "is Smallest")


# 8 Even or odd 
# no=int(input("Enter no:"))
# if no % 2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")


# 9 Check leap year or no 
# year=int(input("Enter year:"))
# if year %4==0:
#     print(year,"year is leap year")
# else:
#     print(year,"is not leap year")







# for loop Programs 

# 1 print natual numbers
# n=int(input("Enter number upto which you want to print natual numbers:"))
# for i in range(1,n+1):
#     print(i)


# 2 print even numbers upto n
# n=int(input("Enter number upto which you want to print even no:"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i)


# 3 print odd numbers upto n
# n=int(input("Enter number upto which you want to print odd no:"))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)


# 4 prints 1 2 4 8 16 ...n^2
# n = int(input("Enter number: "))
# for i in range(n + 1):
#     print(2 ** i)


# 5 Python program to find the sum of the series
# 1 + 1/1! + 1/2! + ... + 1/n!

# n = int(input("Enter the value of n: "))
# sum = 1
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
#     sum += 1 / fact
# print("Sum of the series =", sum)



# 6


# 7 Square root no is prime or not 
# n = int(input("Enter no: "))
# print(n)
# if n > 1:
#     is_prime = True    
#     root = int(n ** 0.5) 
#     for i in range(2, root + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print("Prime number")
#     else:
#         print("Not a prime number")
# else:
#     print("Not a prime number")



# pattern ABC 
# for i in range(1,4):
#     for j in range(65,68):
#         print(chr(j),end='') 
#     print()



# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()



# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()
    

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()



# n = int(input("Enter a number: "))
# for i in range(n,1):
#     for j in range(i):
#         print(j+1, end=" ")
#     print()




# WHILE LOOP PROGRAMS

# 1. Print all natural numbers up to n
# print("1. Natural Numbers")
# n = int(input("Enter n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1

# 2. Print all even numbers up to n
# print("\n2. Even Numbers")
# n = int(input("Enter n: "))
# i = 2
# while i <= n:
#     print(i)
#     i += 2

# 3. Print all odd numbers up to n
# print("\n3. Odd Numbers")
# n = int(input("Enter n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 2

# 4. Sum of natural numbers up to n
# print("\n4. Sum of Natural Numbers")
# n = int(input("Enter n: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print("Sum =", sum)

# 5. Sum of odd numbers up to n
# print("\n5. Sum of Odd Numbers")
# n = int(input("Enter n: "))
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i += 2
# print("Sum =", sum)

# 6. Sum of even numbers up to n
# print("\n6. Sum of Even Numbers")
# n = int(input("Enter n: "))
# i = 2
# sum = 0
# while i <= n:
#     sum += i
#     i += 2
# print("Sum =", sum)

# 7. Print natural numbers in reverse order
# print("\n7. Natural Numbers in Reverse")
# n = int(input("Enter n: "))
# while n >= 1:
#     print(n)
#     n -= 1

# 8. Fibonacci series up to n terms
# print("\n8. Fibonacci Series")
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# count = 1
# while count <= n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1
# print()

# 9. Factorial of a number
# print("\n9. Factorial")
# n = int(input("Enter number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial =", fact)


# 10. Check Prime Number
# print("\n10. Prime Number Check")
# n = int(input("Enter number: "))
# i = 2
# prime = True

# if n <= 1:
#     prime = False
# else:
#     while i < n:
#         if n % i == 0:
#             prime = False
#             break
#         i += 1

# if prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# 11. Sum of digits
# print("\n11. Sum of Digits")
# n = int(input("Enter number: "))
# temp = n
# sum = 0
# while temp > 0:
#     digit = temp % 10
#     sum += digit
#     temp //= 10
# print("Sum of digits =", sum)

# 12. Palindrome Number
# print("\n12. Palindrome Check")
# n = int(input("Enter number: "))
# temp = n
# rev = 0

# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10

# if n == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 13. Reverse a Number
# print("\n13. Reverse Number")
# n = int(input("Enter number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print("Reverse =", rev)


# 14. Multiplication Table
# print("\n14. Multiplication Table")
# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1


# 15. Largest of n Numbers
# print("\n15. Largest of n Numbers")
# count = int(input("How many numbers? "))
# i = 1
# largest = None

# while i <= count:
#     num = int(input("Enter number: "))
#     if largest is None or num > largest:
#         largest = num
#     i += 1

# print("Largest =", largest)


# 16. Smallest of n Numbers
# print("\n16. Smallest of n Numbers")
# count = int(input("How many numbers? "))
# i = 1
# smallest = None

# while i <= count:
#     num = int(input("Enter number: "))
#     if smallest is None or num < smallest:
#         smallest = num
#     i += 1

# print("Smallest =", smallest)
