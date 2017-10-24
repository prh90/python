import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the function!")
    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function")


# my_function()


####
def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("After the decorator")
        return function_that_runs_func
    return my_decorator


# Useful for user permission for websites
# insert elements into db
@decorator_with_arguments(6)
def my_function_too(x, y):
    # print("Hello")
    print(x + y)


my_function_too(57, 67)
