import itertools

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

for house in range (1, 10000000):
    primfactors = prime_factors(house)
    kombis = set(primfactors)

    for idx in range(2,len(primfactors)+1):
        test = itertools.combinations (primfactors, idx)
        for i in test: kombis.add (i)

    final_kombis = set ()
    for k in kombis:
        multi = 1
        if isinstance (k, int):
            final_kombis.add (k)
        else:
            for l in k:
                multi *= l
            final_kombis.add (multi)
    final_kombis.add (1)
    count_final = 0
    for m in final_kombis:
        count_final += m * 10

    if count_final > 29000000:
        break
    print ('House ',house,'got ',count_final,'presents.')
