with open('Advent18Input2.txt') as f:
    src = [x.strip() for x in f.readlines()]
number_cols = len(src[0])
number_rows = len(src)
liste = [[0] * number_cols for i in range(number_rows)]
for idx_i, i in enumerate(src):
    for idx_j, j in enumerate(i):
        liste[idx_i][idx_j] = src[idx_i][idx_j]
print(src)
print(liste)

temp_liste = liste.copy()
temp_liste[0][2] = '!'
print(temp_liste)
print(liste)














