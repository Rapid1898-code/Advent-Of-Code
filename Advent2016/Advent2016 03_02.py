##lines = [["5","10","25"]]
with open ("input03.txt") as f:
    lines = [x.split() for x in f.readlines()]

print(lines)

inp = []
for i in range (0, len(lines), 3):
    for j in range(3):
        row = [lines[i][j], lines[i+1][j], lines[i+2][j]]
        inp.append(row)

count = 0
for i in inp:
    i[0] = int(i[0])
    i[1] = int (i[1])
    i[2] = int (i[2])
    if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]:
        print(i)
        count += 1
print(count)







