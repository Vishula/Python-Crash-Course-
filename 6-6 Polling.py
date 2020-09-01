# Dict with fav languages of people
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    "playboi carti": "Java"
    }
# print out coders and their fav language
for name, fav_lang in favorite_languages.items():
    print(f"Name of the person is {name.title()} and their favourite language is {fav_lang}")
# list of coders who either voted or not
coders = ['phil', 'rakim', 'tyler', 'playboi carti', 'sarah', 'nardwur', 'cardi b']
# check if the coder already voted and print the right message with their name.
for coder in coders:
    if coder in favorite_languages:
        print(f"Thank you for voting {coder.title()}")
    else:
        print(f"Please vote {coder.title()}")