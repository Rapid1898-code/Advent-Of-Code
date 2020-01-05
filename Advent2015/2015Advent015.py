import itertools
inp = []
source = []
maximum = 0

with open('2015Advent015Input.txt') as f:
    liste = [x.strip() for x in f.readlines()]
for i in liste:
    ts = i.split()
    source.extend([[ts[0],int(ts[2][:-1]),int(ts[4][:-1]),int(ts[6][:-1]),int(ts[8][:-1]),int(ts[10])]])

for idx in range (0,100):
    temp_liste = [[a, b-a, 100-idx-b] for a, b in itertools.combinations(range(100-idx), 2)]
    for temp in temp_liste:
        inp.extend([(idx,temp[0],temp[1],temp[2])])

print(source)
for combi in inp:
    tmp1 = combi[0]*source[0][1]+combi[1]*source[1][1]+combi[2]*source[2][1]+combi[3]*source[3][1]
    tmp2 = combi[0]*source[0][2]+combi[1]*source[1][2]+combi[2]*source[2][2]+combi[3]*source[3][2]
    tmp3 = combi[0]*source[0][3]+combi[1]*source[1][3]+combi[2]*source[2][3]+combi[3]*source[3][3]
    tmp4 = combi[0]*source[0][4]+combi[1]*source[1][4]+combi[2]*source[2][4]+combi[3]*source[3][4]
    tempmult = int(tmp1*tmp2*tmp3*tmp4)
    if tempmult > maximum:
        maximum = tempmult
        print(combi,tempmult, tmp1, tmp2, tmp3, tmp4)

print(maximum)