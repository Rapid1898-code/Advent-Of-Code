import itertools

max_value = 0

with open('2015Advent013Input.txt') as f:
    liste = [x.strip() for x in f.readlines()]
inp= {}

for i in liste:
    i = i.split()
    diff = 0
    temp_name1 = i[0][0]
    temp_name2 = i[-1][0]
    if i[2] == 'lose': diff = int(i[3])*(-1)
    elif i[2] == 'gain': diff = int(i[3])
    inp[(temp_name1, temp_name2)] = diff

combis = itertools.permutations('ABCDEFGMI', 9)
#combis = itertools.permutations('ABCD', 4)
# for i in combis:
#     print(i)

for combi in combis:
    temp_max = 0
    if combi[0] != "I" and combi[-1] != "I":
        temp_max += inp[(combi[0], combi[-1])]
        temp_max += inp[(combi[-1], combi[0])]
    for i in range(len(combi)-1):
        if combi[i] != "I" and combi[i+1] != "I":
            temp_max += inp[(combi[i], combi[i+1])]
            temp_max += inp[(combi[i+1], combi[i])]
    if temp_max > max_value: max_value = temp_max


print(max_value)


