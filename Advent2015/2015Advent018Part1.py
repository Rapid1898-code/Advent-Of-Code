import copy

with open('Advent18Input1.txt') as f:
    src = [x.strip() for x in f.readlines()]
number_cols = len(src[0])
number_rows = len(src)
liste = [[0] * number_cols for i in range(number_rows)]
for idx_i, i in enumerate(src):
    for idx_j, j in enumerate(i):
        liste[idx_i][idx_j] = src[idx_i][idx_j]
print(src)
print(liste)

def check_light(x,y):
    count = 0
    if y !=0:   # upper
        if liste[y-1][x] == "#": count += 1
        if x != len(liste[0])-1:  #upper / right
            if liste[y-1][x+1] == "#": count += 1
        if x != 0:  #upper / left
            if liste[y-1][x-1] == "#": count += 1

    if y != len(liste)-1:   # down
        if liste[y+1][x] == "#": count += 1
        if x != 0:  # left / down
            if liste[y+1][x-1] == "#": count += 1
        if x != len(liste[0])-1:   # right / down
            if liste[y+1][x+1] == "#": count += 1

    if x !=0:   # left
        if liste[y][x - 1] == "#": count += 1
    if x != len(liste[0])-1:   # right
        if liste[y][x + 1] == "#": count += 1

    if liste[y][x] == '#':
        if count in [2,3]: return 'ON'
        else: return 'OFF'
    elif liste[y][x] == '.':
        if count == 3: return 'ON'
        else: return 'OFF'
    else: return 'NOTHING'

for anz in range(100):
    temp_liste = copy.deepcopy(liste)
    for idx_r, row in enumerate(liste):
        for idx_c, char in enumerate(row):
            erg = check_light(idx_c,idx_r)
            if erg == 'ON': temp_liste[idx_r][idx_c] = '#'
            elif erg == 'OFF': temp_liste[idx_r][idx_c] = '.'
            else: temp_liste[idx_r][idx_c] = liste[idx_r][idx_c]
    liste = copy.deepcopy(temp_liste)
    print('Step: ',anz+1)
    print(liste)

count_final = 0
for idx_i, i in enumerate(liste):
    for idx_j, j in enumerate(i):
        if liste[idx_i][idx_j] == '#': count_final += 1
print(count_final)













