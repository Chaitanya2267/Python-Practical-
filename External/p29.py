try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))

    result = a / b

    print(result)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("please enter valid number")

finally:
    print("done")