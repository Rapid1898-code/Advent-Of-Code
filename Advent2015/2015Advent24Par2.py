import itertools

erg = [1,3,5,11,13,17,19,23,29,31,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
target = 387

arr = []
for r in range(1,len(erg)-2):
    found = False
    for i in itertools.combinations(erg, r):
        if sum(i) == target:
            print(i)
            arr.append(i)
            found = True
    if found == True: break

end_min = 9999999999999999999999999
def prod(it):
    p = 1
    for i in it:
        p *= i
    return p

for i in arr:
    end_min = min(end_min, prod(i))

print (len (arr))
print (end_min)
















