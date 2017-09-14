def factorial(n):
    """ Calculate n! recursively """
    if n<=1:
        return 1
    else:
        return n * factorial(n-1)


# print(factorial(25))
try:
    print(factorial(1000))
except RecursionError:
    print("This program can't calculate factorials that large.")

print("Program terminated")
