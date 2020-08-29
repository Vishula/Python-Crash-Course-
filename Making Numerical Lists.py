# MAKING NUMERICAL LISTS

# range() - generate series of numbers like 1.2.3.4.5
# c = 0
# for values in range(1,6):
#     c = c + 1
#     print(c,".line ", values)


# range() to make a list of Numbers

# square numbers

# sq = []
# for vals in range(1,12):
#     square = vals**2
#     sq.append(square)
#
# print(sq)

# 1-10 * 2

# num = []
# for vals in range(1,11):
#     x = (vals * 2) + 69
#     num.append(x)
#
# print(num)

# 1 to million

# mil = []
# for nums in range(1,1000000):
#     mil.append(nums)
#
# #print(mil)
# print("Sum num is ", sum(mil))


# SQ without list comprehension
# example 1
# sq = []
# for numbers in range(1,25):
#     num = numbers ** 2
#     sq.append(num)
# print(sq)

# example 2
# trio = []
# for vals in range(1,15):
#     value = vals ** 3
#     trio.append(value)
# print(trio)
# print(sum(trio))
#
#
# trio = [vals ** 3 for vals in range(1,15)]
# print(trio)

# SQ with List comprehension
# first begin with descriptive name of the list such as squares
# then open set of [] brackets and define the EXPRESSION for
# the numbers you want to store in the list
#
# squares = [numbers ** 2 for numbers in range(1,10)]
# print(squares)






