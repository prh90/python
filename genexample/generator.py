def odd_numbers():
    current = 1
    while True:
        yield current
        current += 2


def pi_series():
    odds = odd_numbers()
    approximation = 0
    while True:
        approximation += (4/ next(odds))
        yield approximation
        approximation -= (4/next(odds))
        yield approximation


approx_pi = pi_series()

for x in range(100000):
    print(next(approx_pi))
