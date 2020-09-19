# input() function example
name = input("What is your name: ")
# use f-string format to print the name variable and a string
print(f"User's name is {name.title()}")


# Using int() to convert string input to int
age = int(input("Please enter your age: "))

if age>18:
    print("Adult")
else:
    print("kid")

