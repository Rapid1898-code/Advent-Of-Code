import itertools

def SumTheList(thelist, target):
    arr = []
    p = []
    if len(thelist) > 0:
        for r in range(0,len(thelist)+1):
            arr += list(itertools.combinations(thelist, r))

        for item in arr:
            if sum(item) == target:
                p.append(item)

    return p

erg = SumTheList([1,2,3,4,5,7,8,9,10,11], 20)
print(erg)