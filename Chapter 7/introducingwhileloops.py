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