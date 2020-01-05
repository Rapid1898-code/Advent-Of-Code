with open('2015Advent017Input1.txt') as f:
    liste = [int(x.strip()) for x in f.readlines()]
target=150
solutions_count = 0
solutions_list = []
#liste=[20,15,10,5,5]

def subsets_with_sum(lst, target, with_replacement=False):
    x = 0 if with_replacement else 1
    def _a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(lst)):
            _a(u + x, l + [lst[u]], r, t)
        return r
    return _a(0, [], [], target)

erg = subsets_with_sum(liste,target)

minimum=999
for combi in erg:
    if len(combi) < minimum: minimum = len(combi)
print(minimum)

count=0
for combi in erg:
    if len(combi) == 4: count += 1
print(count)




