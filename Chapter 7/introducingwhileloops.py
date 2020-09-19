# While loop in action
# Following while loop counts from 0 to 10 in 2 increments

currentnum = 0

while currentnum < 10:

    print(currentnum)
    currentnum +=2


# While loop in action until user enters QUIT

# prompt = question asking user
prompt = 'Tell me something and i will repeat back to you.'
prompt += ' Enter "Quit" to end the program: '
# empty string to store user input
message = ''
# while loop runs until user enters quit
while message != 'quit':
    message = input(prompt) # asks user the question
    print(message) # print user input

# Above program works but it prints quit as well when you want to exit out of the
# program

# Simple FIX - will do a different program so i can use dem skills g

# empty string to store user values
story = ''

while story != 'quit':
    story = input("Enter your story: ")
    if story != 'quit':
        print(story)

