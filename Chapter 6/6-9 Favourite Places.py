# Vishula - Redo this in 15 mins

# Make a dictionary called favourite_places
# 3 names use as keys - In the dictionary
# name 3 favourite places for each person/names


# list inside of a dictionary
# use a list to ([3 favourite places inside a list]) later you can iterate through it
favourite_places = {"dave2d ":["new york", "Japan","german"],
                    "mkbhd":["tokyo", "Sri lanka","greece"],
                    "linus":["england","africa","china"]}

# for one_youtuber in favourite_places:
#     if one_youtuber == "mkbhd":
#         print(f"Youtuber name: {one_youtuber} ".title())
#
#     else:
#         print(f"Youtuber name: {one_youtuber} ".title())
print("Locations for Dave 2D")
for places in favourite_places["dave2d "]:
    print(f"{places}")
print("Locations for mkbhd ")
for places in favourite_places["mkbhd"]:
    print(f"{places}")
print("Location for Linus")
for places in favourite_places["linus"]:
    print(f"{places}")






