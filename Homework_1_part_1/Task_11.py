def tribonacci_generator():
    trib1 = 0
    trib2 = 1
    trib3 = 1
    yield trib1
    yield trib2
    yield trib3

    while True:
        trib1, trib2, trib3 = trib2, trib3, trib1 + trib2 + trib3
        yield trib3

gen = tribonacci_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))