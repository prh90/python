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


# Could pass it in as arg and use it
# def print_backwards(*args, end=' ',**kwargs):
# can remove it from dictionary kwargs
# def print_backwards(*args, **kwargs):
#     kwargs.pop('end', None)
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end, **kwargs)

def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    print(kwargs)
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)

with open("backwards.txt", "w") as backwards:
    print_backwards("Hello", "Planet", "Earth", end="\n")
    print("Another string")


print("*"*50)
print("Hello", "Planet", "Earth", end='', sep='\n**\n')
print_backwards("Hello", "Planet", "Earth", end='', sep='\n**\n')
print("*"*50)




# *args unpacks a tuple or a list
# **kwargs unpacks a dictionary

