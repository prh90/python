def fibonacci():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current


fib = fibonacci()
run = range(21)

for i in run:
    print(next(fib))

