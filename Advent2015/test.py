from itertools import combinations
# >>> [comb for i in range(1, 20) for comb in combinations(vals, i) if sum(comb) == target]
# [(114, 156), (57, 99, 114)]

vals = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
target = 270
result = []
# for i in range(1,20):
#     for comb in combinations(vals,i):
#         if sum(comb) == target: result.append(comb)
#
# print(result)

for comb in combinations (vals,2):print(comb)














