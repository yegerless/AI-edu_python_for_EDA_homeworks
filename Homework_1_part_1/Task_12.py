def cyclic_shift(s):
    for _ in range(len(s)):
        yield s
        s = s[1:] + s[0]

for seq in cyclic_shift("abcdef"):
    print(seq)