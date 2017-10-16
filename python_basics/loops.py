my_variable = "hello, world"

# print(my_variable[0])

# for character in my_variable:
# iterables are strings, lists, sets, tuples and more
#     print(character)

my_list = [1, 3, 5, 7, 9]

# for i in my_list:
#     print(i ** 2)

user_wants_number = True

while user_wants_number == True:
    print(10)

    user_input = input("Should we print again? (y/n) ")
    # if user_input == "y":
    #     user_wants_number = True
    # elif user_input == "n":
    #     user_wants_number = False
    if user_input == "n":
        user_wants_number = False
