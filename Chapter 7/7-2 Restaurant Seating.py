# program that asks the user how many people are in their dinner group.
# if number is bigger than 8, print they have to wait for a table and -
# otherwise report their table is ready.

# use int function at the start to convert use input string to an int
numberofpeople = int(input("How many people are in your dinner group? "))

# if loop to print correct statment
if numberofpeople > 8:
    print("Sorry you have to wait for a table :(")
else:
    print("You're table is ready. Please check in :) ")