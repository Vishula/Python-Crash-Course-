# 3-4 GUEST LIST

invitationlist = ['asap rocky', 'playboi carti', 'lil uzi vert']

# print(f"{invitationlist[0]} is invited to the dinner")
# print(f"{invitationlist[1]} is invited to the dinner")
# print(f"{invitationlist[2]} is invited to the dinner")

# for artist in invitationlist:
#     print(f"{artist} is invited to the dinner")

# 3-5 Changing GUEST LIST

cantmakeit = invitationlist.pop(1)
print(f"{cantmakeit} unfortunately can't make it for the dinner.")
invitationlist.append('kayne west')
print("New invitation list is", invitationlist)
for artist in invitationlist:
    print(f"{artist} is invited to the dinner. ")

print("----"*20)
# 3-6 More GUESTS

# moreguests = ['kodak black', '21 savage', 'denzel curry']
# invitationlist.extend['kodak black', '21 savage', 'denzel curry']
# print(invitationlist)

invitationlist.insert(1,'kodak vlack')
invitationlist.insert(4,'21 savage')
invitationlist.append('denzel curry')
print("Extended Guest List is ", invitationlist)

for artist in invitationlist:
    print(f"{artist} is invited to the dinner. ")

# 3-7 Shrinking GUEST LIST

print("x-x-"*20)
print("Only 2 spots left")
print("Current invitation list = ", invitationlist)
out = invitationlist.pop(0)
print(f"{out} is no longer invited")
# print(invitationlist)
out = invitationlist.pop(0)
print(f"{out} is no longer invited")
# print(invitationlist)
out = invitationlist.pop(0)
print(f"{out} is no longer invited")
# print(invitationlist)
out = invitationlist.pop(0)
print(f'{out} is no longer invited')
# print(invitationlist)
# it seems like every time you have to 0 it to delete the first element

print(f"{invitationlist[0]} is still invited")
print(f"{invitationlist[1]} is still invited")

print("PARTY ENDED SO IM GOING TO DEL EVERYONE")
del invitationlist[:]
print(invitationlist)

#



