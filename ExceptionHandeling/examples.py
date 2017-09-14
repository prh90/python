def factorial(n):
    """ Calculate n! recursively """
    if n<=1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)


# print(factorial(25))
# can combine errors if the message being returned can make sense for both else
# use separate messages with error handling.
try:
    print(factorial(900))
except RecursionError:
    print("This program can't calculate factorials that large.")
except ZeroDivisionError:
    print("Cant divide by zero son")
print("Program terminated")
