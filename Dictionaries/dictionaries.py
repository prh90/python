fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# print(fruit.items())

f_tuple = tuple(fruit.items())
# print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
# **************************************
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"] = "an odd shaped apple"
# print(fruit)

# # Deletes a specific key and value
# del fruit["pear"]
# print(fruit)

# deletes the whole dictionary/hash
# del fruit

# clears all info in hash but maintains variable
# fruit.clear()
# print(fruit)
#
# while True:
#     dict_key = input("Please Enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("We do not have that")
# *******************************************
# while True:
#     dict_key = input("Please Enter a fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have " + dict_key)
#     print(description)
    # if dict_key in fruit:
    #     description = fruit.get(dict_key)
    #     print(description)
    # else:
    #     print("We do not have that")
