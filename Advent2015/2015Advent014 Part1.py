with open('2015Advent014Input.txt') as f:
    liste = [x.strip().split() for x in f.readlines()]
inp = []
for i in liste: inp.extend([[i[0],int(i[3]),int(i[6]),int(i[-2])]])

def check_distance(sek, km, sek_drive, sek_rest):
    temp_rest = sek % (sek_drive+sek_rest)
    temp_anz = sek // (sek_drive+sek_rest)
    if temp_rest > sek_drive: return((temp_anz+1) * sek_drive * km)
    elif temp_rest <= sek_drive: return((temp_anz * sek_drive * km) + temp_rest)

for i in inp:
    print(i[0], check_distance(2503, i[1], i[2], i[3]))