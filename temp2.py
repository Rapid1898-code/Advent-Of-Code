import math

def calcLCM(a, b):
    return abs(a*b) // math.gcd(a, b)

# erg = lcm(5, 6)
# print(erg)


a = [100, 200, 150, 455, 3232]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:

    print(f"LCM: {lcm}")
    print(f"I: {i}")

    lcm = calcLCM(lcm, i)
print(lcm)
