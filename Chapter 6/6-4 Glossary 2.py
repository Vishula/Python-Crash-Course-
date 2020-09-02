# Redo exercise 6-3(page 99) by replacing your series of print() calls with a loop that runs throgh the dict keys and
# values.
print("Python Glossary Terms")
glossary = {">>>": "This is the default prompt of the Python interactive shell",
            "immutable": "An object with fixed value. Immutable objects include numbers, strings and tuples.",
            "list comprehension" : "A neat syntactical way to process elements in a sequence and return a list with "
                                   "results.",
            "dictionary" : "dictionary is a variable that can store values of multiple types"}

print("dict ", glossary["dictionary"] )
print(">>> ", glossary[">>>"])