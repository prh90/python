def my_method(arg1, arg2):
    return arg1 + arg2


def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6


def my_list_addition(list_arg):
    return sum(list_arg)


##
# *args this is a list of arguments that have been passed to the method
def addition_simplified(*args):
    return sum(args)


# print(addition_simplified(3, 5, 7, 12, 14, 55))

##


def what_are_kwargs(*args, **kwargs):
    print(args)  # You get a tuple of arguments
    print(kwargs)  # empty set


# When this is passed it is parsed automatically
what_are_kwargs(12, 34, 56, name='Jose', location='UK')
