# sorted()
# Empty list
people = []
# make a person
person = {"fname":"karl",
         "lname":"james",
         "city":"new york",
           }
# append the person to list
people.append(person)

person = {"fname":"sarah",
           "lname":"tim",
           "city":"brisbane"}
# append the person to list
people.append(person)

person = {"fname":"ken",
           "lname":"azura",
           "city":"tokyo"}
# append the person to list
people.append(person)

for person in people:
    name = person['fname']
    lname = person['lname']
    city = person['city']

    print(f"His name is {name} {lname} and he's from {city}")
