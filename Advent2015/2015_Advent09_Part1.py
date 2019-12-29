import itertools
input = []; mindist = 9999999

with open('Advent09.txt') as f:
    lines = [x.strip().split() for x in f.readlines()]
for entry in lines:
    if entry[0][0:2] < entry[2][0:2]: input.append([entry[0][0:2],entry[2][0:2],entry[4]])
    else: input.append([entry[2][0:2],entry[0][0:2],entry[4]])
combis = list(itertools.permutations(('Tr','Al','Sn','Ta','Fa','No','St','Ar'), 8))

#combis = list(itertools.permutations(('Lo','Du','Be'),3))
#input = [['Lo', 'Du', '464'], ['Lo', 'Be', '518'], ['Du', 'Be', '141']]

print(input)
print(combis)


def find_distance(dest1, dest2):
    for entry in input:
        if (dest1 == entry[0] and dest2 == entry[1]) or (dest2 == entry[0] and dest1 == entry[1]):
            return int(entry[2])

for combi in combis:
    idx=0
    temp_sum=0
    while idx < len(combi)-1:
        temp_sum += find_distance(combi[idx], combi[idx+1])
        idx += 1
    mindist = min(mindist,temp_sum)

print(mindist)




