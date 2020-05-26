#lines = ["ULL","RRDDD","LURDL","UUUUD"]
with open ("input02.txt") as f:
    lines = [x.strip() for x in f.readlines()]
print(lines)

pos = 5
erg = ""
for i in lines:
    for j in i:
        if j == "U" and pos in [1, 2, 3]: continue
        if j == "D" and pos in [7, 8, 9]: continue
        if j == "L" and pos in [1, 4, 7]: continue
        if j == "R" and pos in [3, 6, 9]: continue
        if j == "U": pos -= 3
        if j == "D": pos += 3
        if j == "L": pos -= 1
        if j == "R": pos += 1
    erg += str(pos)
print(erg)





