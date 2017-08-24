def fact(n):
    """ calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

# for i in range(130):
#     print(i, fact(i))
# confused but the result storage
# just take a look at the *=
# it takes what is stored and multiplies it
# with the next digit


def factorial(n):
    # n! can also be defined as n * (n-1)
    """ calculates recusively """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# for i in range(130):
#     print(i, factorial(i))

def fib(n):
    """ F(n) = F(n - 1) + F(n - 2) """
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

# for i in range(36):
#     print(i, fib(i))


def fibonacci(n):
    """ Recursive fib """
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_minus1 = 1
        n_minus2 = 0
        for f in range(1, n):
            result = n_minus2 + n_minus1
            n_minus2 = n_minus1
            n_minus1 = result
    return result

for i in range(36):
    print(i, fibonacci(i))
