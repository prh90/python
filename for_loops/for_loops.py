# For loops intro


# for i in range(1, 20):
#     print("i is now {}".format(i))
# #
# number = "9, 223, 372, 036, 854, 775, 807"
# for i in range(0, len(number)):
#     print(number[i])

# number = "9, 223, 372, 036, 854, 775, 807"
# cleanedNumber = ''
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber = cleanedNumber + number[i]
#
# newNumber = int(cleanedNumber)
# print(newNumber)
# ############################################################

# number = "9, 223, 372, 036, 854, 775, 807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
# newNumber = int(cleanedNumber)
# print("new num = {}".format(newNumber))

# A way to iterate through an array
# for state in ["not pinin'", "no more", "a stiff", "bereft of life"]:
#     print("This parrot is " + state)
#   You can also use
#   print("This parrot is {}".format(state)

# for i in range(0, 100, 5):
#     print("i is {}".format(i))
# Nested loops is next

# for i in range(1, 13):
#     for j in range(1,13):
#         print("{1} time {0} is {2}".format(i, j, i*j))
#     print("++++++++++++++++++++++")