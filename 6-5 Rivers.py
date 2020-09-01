# make a dictionary containing 3 major rivers and
# their country of origin
# One kay has to be 'nile':'egypt'[last key value pair]

# Rivers dict defining name of the river as key and origin as values.
rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

# use items method to get all the key-value pairs from dict.
# use f" formatting
# use count to number the list
for river, origin in rivers.items():
    print(f"The river {river} flows through {origin}")
count = 0
print("Rivers in the list are: ")
for river in rivers.keys():
    count+=1
    print(f"{count}. {river}")
coun = 0
print("Origins in this list are: ")
for origin in rivers.values():
    coun+=1
    print(f"{coun}. {origin}")


