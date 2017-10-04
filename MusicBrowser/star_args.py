def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


# args short for arguments
# *args takes all that is fed

def build_tuple(*args):
    return args


# print(average(1, 2, 3, 4))
number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)
