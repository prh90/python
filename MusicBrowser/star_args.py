# def average(*args):
#     print(type(args))
#     print("args is {}:".format(args))
#     print("*args is:", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# # args short for arguments
# # *args takes all that is fed
#
# def build_tuple(*args):
#     return args
#
#
# # print(average(1, 2, 3, 4))
# number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
# print(type(number_tuple))
# print(number_tuple)


# def print_backwards(*args, file=None):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', file=file)
def print_backwards(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)



with open("backwards.txt", "w") as backwards:
    print_backwards("Hello", "Planet", "Earth", file=backwards)

# *args unpacks a tuple or a list
# **kwargs unpacks a dictionary

