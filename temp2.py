import itertools

l = [5,6,11]
# for i in itertools.combinations(l, 3): print(i)
# for i in itertools.combinations(l,3): print(i)
print(list(itertools.permutations(l,3)))



