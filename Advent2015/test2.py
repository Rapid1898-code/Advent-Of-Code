def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n

x = 123
erg = bit_not(x)
print(erg)

