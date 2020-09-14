favourite_numbers = {"mark":[22,69,38],
                     "delis":[11,23,9],
                     "ken":[87,71,15],
                     "tyler":[9900,1120,9999],
                     "Piper":[420,422,425]}

for name,highestscores in favourite_numbers.items():
    print(f"Name of the person is {name.title()} and their favourite numbers ")
    print(f"Display Data:")
    for highestscore in highestscores:   # iterating through highscores
        print(f"\t\t\t{highestscore}")


# for person in favourite_numbers:
#     print(person)
#     if person in favourite_numbers["mark"]:
#         print(person)
#for person in favourite_numbers:

# tv = []
# for name,nums in favourite_numbers.items():
#     for num in nums:
#         tv.append([nums])

# print(tv)
# d = {'ANIMAL' : ['CAT','DOG','FISH','HEDGEHOG']}
# d_list = []
# for key, values in d.iteritems():
#     for value in values:
#         d_list.append([key, value])

# for name,nums in favourite_numbers.items():
#     print(f"Name of the person is {name.title()} Numbers they like ")
#     for number in nums:
#         print(f"{number}")
