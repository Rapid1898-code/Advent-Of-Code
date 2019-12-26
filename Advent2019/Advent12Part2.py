from math import gcd
#pos = [[0,[-7,-1,6]], [1,[6,-9,-9]], [2,[-12,2,-7]], [3,[4,-17,-12]]]
#pos = [[0,[-8,-10,0]], [1,[5,5,10]], [2,[2,-7,3]], [3,[9,-8,-3]]]
#pos = [[0,[-1,0,2]], [1,[2,-10,-7]], [2,[4,-8,8]], [3,[3,5,-1]]]
#vel = [[0,[0,0,0]], [1,[0,0,0]], [2,[0,0,0]], [3,[0,0,0]]]

#pos = [[-7,6,-12,4],[-1,-9,2,-17],[6,-9,-7,-12]]
#pos = [[-1,2,4,3],[0,-10,-8,5],[2,-7,8,-1]]
pos = [[-8,5,2,9],[-10,5,-7,-8],[0,10,3,-3]]
ergebnisse = []

for z in range(3):
    testp = list(pos[z])
    testv = [0, 0, 0, 0]
    states = []
    count = 1
    while pos[z] not in states:
        for i in range(4):
            tmp_count = 0
            for j in range(4):
                if i==j: continue
                else:
                    if testp[i] > testp[j]: tmp_count -= 1
                    elif testp[i] < testp[j]: tmp_count += 1
            testv[i] += tmp_count
        for i in range(4): testp[i] += testv[i]
        count += 1
        if count % 1000 == 0: print(count)
        states.append(list(testp))
    ergebnisse.append(count)

    lcm = ergebnisse[0]
    for i in ergebnisse[1:]:
        lcm = lcm*i//gcd(lcm, i)
print(ergebnisse)
print(lcm)