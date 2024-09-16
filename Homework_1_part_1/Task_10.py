def fibonacci():
    fib1 = 0
    fib2 = 1
    yield fib1
    yield fib2

    while True:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2

gen = fibonacci()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))