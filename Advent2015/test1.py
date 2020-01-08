import itertools
primfactors = [2,2,2,5]
kombis = set(primfactors)

test = itertools.combinations(primfactors,2)
test2 = itertools.combinations(primfactors,3)
test3 = itertools.combinations(primfactors,4)
for i in test: kombis.add(i)
for j in test2: kombis.add(j)
for j in test3: kombis.add(j)

final_kombis = set()
for k in kombis:
    multi = 1
    if isinstance(k,int): final_kombis.add(k)
    else:
        for l in k:
            multi *= l
        final_kombis.add(multi)
final_kombis.add(1)
count_final = 0
for m in final_kombis:
    count_final += m*10

print(kombis)
print(final_kombis)
print(count_final)







