# string = "123456789"
#
# # for char in string:
# #     print(char)
# my_iterator = iter(string)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))

# for char in string:
#     print(char)
#
# for char in iter(string):
#     print(iter)

# Mini Challenge
my_list = ["spam", "eggs", "bacon", "steak"]

my_iterator = iter(my_list)
rounds = len(my_list)

# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
for item in range(0,len(my_list)):
    print(next(my_iterator))

# my_list = {"Monday", "Tuesday", "Wed", "Thurs", "Friday", "Sat", "Sun"}
# my_iterator = iter(my_list)
#
# for i in range(0, len(my_list)):
#     next_item = next(my_iterator)
#     print(next_item)