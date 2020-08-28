# rappers = ['asap rocky', 'playboi carti', 'lil uzi vert',
#            '21 savage', 'kodak black', 'denzel curry','zendaya']
#
# print("Listen Out First day[ Line-up: ")
# for rapper in rappers[0:3]:
#     print(rapper.title())
# print("Listen Out Second day Line-up:" )
# for rapper in rappers[3:5]:
#     print(rapper.title())
# print("Listen Out Third day Line-up")
# for rapper in rappers[5:]:
#     print(rapper.title())

my_fav_artists = ['asap rocky', 'playboi carti', 'lil uzi vert']
friend_fav_artists = my_fav_artists[:]
my_fav_artists = friend_fav_artists
my_fav_artists.append("boggie wit da hoodie")
friend_fav_artists.append("pusha T")



print(f"My favourite artist: {my_fav_artists} ")
print(f"\nMy friend's favourite artists: {friend_fav_artists}")


# Copying list - use slice [:] to do it
# my_food = ['apple', 'banana']
# friend_food = my_food[:]




# if my_fav_artists == friend_fav_artists:
#     print("TRUE")
# else:
#    print("FALSE")




