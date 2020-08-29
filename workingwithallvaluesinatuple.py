# 4-10 Slices
rappers = ['asap rocky', 'playboi carti', 'lil uzi vert',
           '21 savage', 'kodak black', 'denzel curry','zendaya','pusha T','asap ferg']

print("First 3 items in the list")
for rapper in rappers[0:3]:
    print(rapper.title())
print("3 items from the middle")
for rapper in rappers[3:6]:
    print(rapper.title())
print("last 3 items of the list")
for rapper in rappers[6:]:
    print(rapper.title())

# 4-11 My pizzas, your pizzas

my_pizzas = ['bbq ', 'ham', 'cheese & garlic']
friend_pizzas = my_pizzas[:]
my_pizzas.append('kottu')
friend_pizzas.append('pork')
print('My favourite pizzas are: ')
for pizza in my_pizzas:
    print(f'{pizza.title()}')
print("My friend's fav pizza are: " )
for pizza in friend_pizzas:
    print(f"{pizza.title()}")

# 4-12 More loops

