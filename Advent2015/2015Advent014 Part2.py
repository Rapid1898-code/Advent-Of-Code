with open('2015Advent014Input2.txt') as f:
    liste = [x.strip().split() for x in f.readlines()]
inp = []
distance = []
points = {}

for i in liste:
    inp.extend([[i[0],int(i[3]),int(i[6]),int(i[-2])]])
    distance.extend([[i[0],0]])
    points[i[0]] = 0

def check_distance(sek, km, sek_drive, sek_rest):
    temp_rest = sek % (sek_drive+sek_rest)
    temp_anz = sek // (sek_drive+sek_rest)
    if temp_rest > sek_drive: return((temp_anz+1) * sek_drive * km)
    elif temp_rest <= sek_drive: return((temp_anz * sek_drive * km) + temp_rest * km)

for sekunde in range(1000):
    for idx, horse in enumerate (inp):
        distance[idx][1] = check_distance(sekunde, horse[1], horse[2], horse[3])
    temp_list = list(distance)
    temp_list.sort(key=lambda x: x[1], reverse=True)
    idx=0
    points[temp_list[idx][0]] += 1
    while temp_list[idx+1][1] == temp_list[idx][1]:
        points[temp_list[idx+1][0]] += 1
        idx += 1
        if idx+1 == len(temp_list): break
    print(sekunde, points, distance, temp_list)
    # print(sekunde, points)