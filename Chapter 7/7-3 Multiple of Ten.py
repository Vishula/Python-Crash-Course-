# Ask the user for a number and then report whether the number is a
# multiple of 10 or not

# here you have to use modulo operator to find if its multiple by 10

number = int(input("Enter a number "))

# if the desired number has 0 as a remainder  it means its a multiple of 10
if number % 10 == 0:
    print(f"Number {number} is a multiple of 10")
else:
    print(f"Number {number} is not a multiple of 10")