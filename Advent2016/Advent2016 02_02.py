#lines = ["ULL","RRDDD","LURDL","UUUUD"]
with open ("input02.txt") as f:
    lines = [x.strip() for x in f.readlines()]
print(lines)

pos = 5
erg = ""
for i in lines:
    for j in i:
        if j == "U" and pos in [5,2,1,4,9]: continue
        if j == "D" and pos in [5,10,13,12,9]: continue
        if j == "L" and pos in [1,2,5,10,13]: continue
        if j == "R" and pos in [1,4,9,12,13]: continue
        if j == "U":
            if pos in [3,13]: pos -= 2
            else: pos -= 4
        if j == "D":
            if pos in [1,11]: pos += 2
            else: pos += 4
        if j == "L": pos -= 1
        if j == "R": pos += 1

    print(pos)

    char = str(pos)
    if char == "10": char = "A"
    if char == "11": char = "B"
    if char == "12": char = "C"
    if char == "13": char = "D"
    erg += char
print(erg)





