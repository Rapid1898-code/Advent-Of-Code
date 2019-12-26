pos = [[0,[-7,-1,6]], [1,[6,-9,-9]], [2,[-12,2,-7]], [3,[4,-17,-12]]]
#pos = [[0,[-8,-10,0]], [1,[5,5,10]], [2,[2,-7,3]], [3,[9,-8,-3]]]
#pos = [[0,[-1,0,2]], [1,[2,-10,-7]], [2,[4,-8,8]], [3,[3,5,-1]]]
vel = [[0,[0,0,0]], [1,[0,0,0]], [2,[0,0,0]], [3,[0,0,0]]]

def check_vel(nr, check_pos):
    count = [0, 0, 0]
    for i in check_pos:
        if i[0] == nr: continue
        else:
            if check_pos[nr][1][0] > i[1][0]: count[0] -= 1
            elif check_pos[nr][1][0] < i[1][0]: count[0] += 1
            if check_pos[nr][1][1] > i[1][1]: count[1] -= 1
            elif check_pos[nr][1][1] < i[1][1]: count[1] += 1
            if check_pos[nr][1][2] > i[1][2]: count[2] -= 1
            elif check_pos[nr][1][2] < i[1][2]: count[2] += 1
    return(count)

kin_energie = 0
pot_energie = 0

for i in range(1000):
    for j in vel:
        a,b,c = check_vel (j[0], pos)
        j[1][0] += a
        j[1][1] += b
        j[1][2] += c

    for j in range (len(pos)):
        for k in range (len(pos)-1):
            pos[j][1][k] += vel[j][1][k]
for i in range(len(pos)):
    print(pos[i], vel[i])

summe = 0
for i in range(4):
    sum_pos = (abs(pos[i][1][0]) + abs(pos[i][1][1]) + abs(pos[i][1][2])) * (abs(vel[i][1][0]) + abs(vel[i][1][1]) + abs(vel[i][1][2]))
    print(sum_pos)
    summe += sum_pos

print('Summe:',summe)









