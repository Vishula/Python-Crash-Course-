active = True

while active:
    topping = input("Enter the pizza topping you need to add: ")
    if topping == 'quit':
        active = False # Use of flag to stop the loop
    else:
        print(topping, ' is added..')



