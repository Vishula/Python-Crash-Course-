# List inside a dictionary

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }
for fname, favlang in favorite_languages.items():
 print(fname + "'s favorite languages are:")

 for fav in favlang:
  print(f"\t {fav.title()}")


