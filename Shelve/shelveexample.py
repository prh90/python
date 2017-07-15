import shelve

# A shelve is a read/write by nature
# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange, citrus, fruit"
#     fruit['apple'] = "good for making cider"
#     fruit['lemon'] = "a sour , yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
#     fruit["lime"] = "great with tequila"
#
#     for snack in fruit:
#         print(snack + ": " + fruit[snack])

# If code is outside the with statement you receive an error because the 'with' closes the loop as soon as block ends
#############################################
# This is the manual way to open and close

fruit = shelve.open('ShelfTest')
# once you save it into shelf then when you rerun it will rewrite the shelf

# fruit['orange'] = "a sweet, orange, citrus, fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "a sour , yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
# # this is to explicitly tell it to close
# while True:
#     dict_key = input("please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have {}".format(dict_key))

for f in fruit:
    print(f + " - " + fruit[f])

fruit.close()