##inp = ["R8", "R4", "R4", "R8"]

str = "R4, R5, L5, L5, L3, R2, R1, R1, L5, R5, R2, L1, L3, L4, R3, L1, L1, R2, R3, R3, R1, L3, L5, R3, R1, L1, R1, R2, L1, L4, L5, R4, R2, L192, R5, L2, R53, R1, L5, R73, R5, L5, R186, L3, L2, R1, R3, L3, L3, R1, L4, L2, R3, L5, R4, R3, R1, L1, R5, R2, R1, R1, R1, R3, R2, L1, R5, R1, L5, R2, L2, L4, R3, L1, R4, L5, R4, R3, L5, L3, R4, R2, L5, L5, R2, R3, R5, R4, R2, R1, L1, L5, L2, L3, L4, L5, L4, L5, L1, R3, R4, R5, R3, L5, L4, L3, L1, L4, R2, R5, R5, R4, L2, L4, R3, R1, L2, R5, L5, R1, R1, L1, L5, L5, L2, L1, R5, R2, L4, L1, R4, R3, L3, R1, R5, L1, L4, R2, L3, R5, R3, R1, L3"
inp = str.replace(" ","").split(",")

dir = "n"
x_axis = y_axis = 0
visit = [(0,0)]

for i in inp:
    if i[0] == "R":
        if dir == "n": dir = "o"
        elif dir == "o": dir = "s"
        elif dir == "s": dir = "w"
        elif dir == "w": dir = "n"
    if i[0] == "L":
        if dir == "n": dir = "w"
        elif dir == "o": dir = "n"
        elif dir == "s": dir = "o"
        elif dir == "w": dir = "s"
    for j in range (int (i[1:])):
        if dir == "n": y_axis += 1
        elif dir == "s": y_axis -= 1
        elif dir == "o": x_axis += 1
        elif dir == "w": x_axis -= 1
        if (x_axis, y_axis) in visit: break
        visit.append((x_axis,y_axis))
print("x: ", x_axis)
print("y: ", y_axis)
print(visit)
print ("Distance:", abs(x_axis)+abs(y_axis))
