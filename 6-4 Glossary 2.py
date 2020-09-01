#

import random
count = 0

glossary = {"Lambda":"A lambda is an anonymous inline function made of a single expression. When we call the "
                        "function, it evaluates the expression and returns it.",
            "List":"A list is a sequence of objects. This sequence is mutable, and can be heterogeneous.",
            "List Comprehension":"A list comprehension is a compact way to create a list.",
            "Method":"A method is simply a function we define inside a class body. We provide ‘self’ as the first "
                     "parameter to each method; it is how it understands that it must work with this object. For more "
                     "on methods, read up on Python Methods.",
            "Mutable":"Unlike immutables, a mutable can change its value. However, it keeps its id(). Examples include "
                      "lists and dictionaries.",
            "Error File":"In Python, we can refer to a variable in an enclosing definition. An inner function can refer to "
               "variables in the outer function. But when we say refer, we mean it can access that variable to read it,"
               " but cannot modify it. Refer to Namespaces in Python for this.",
            "icloud":"When you sign up for iCloud, you automatically get 5GB of free storage"}

print(f"Printing Keys \n:")
for word in glossary.keys():
    count+=1
    print(count, word)

print("Printing Values\n: ")
for word in glossary.values():
    word.isalpha()
    print(word)




