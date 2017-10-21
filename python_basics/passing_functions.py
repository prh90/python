def methodception(another):
    return another()


def add_two_numbers():
    return 35 + 77


# print(methodception(add_two_numbers))

# print(methodception(lambda: 35 + 77))

my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x % 2 == 1, my_list)))
# left to right meanning we are running a function agains a list

# list comprehension
print([x for x in my_list if x != 13])

#####
# (lambda x: x * 3)(5)
#
#
# # is equal to
# def f(x):
#     return x * 3
#
#
# f(5)
