lines = ["rect 3x2","rotate column x=1 by 1","rotate row y=0 by 4","rotate column x=1 by 1"]
#with open("input08.txt") as f:
#    lines = [x.strip() for x in f.readlines()]

x_def = 7
y_def = 3
#x_def = 50
#y_def = 6
scr = [["." for x in range(x_def)] for x in range(y_def)]

for l in lines:
    if "rect" in l:
        l = l.replace("rect ","")
        for idx,cont in enumerate(l):
            if cont == "x":
                x = int(l[:idx])
                y = int(l[idx+1:])
        for i in range(y):
            for j in range(x): scr[i][j] = "#"

        print(scr)

    elif "rotate row" in l:
        l = l.replace("rotate row ","")
        tmp_pos_y = l.find("y=") + 2
        tmp_end_y = l.find ("by ")
        tmp_by = l.find ("by ") + 3
        y = int(l[tmp_pos_y:tmp_end_y])
        by = int(l[tmp_by:].strip())
        for i in range(by):
            last_char = scr[y][x_def-1]
            scr[y].pop()
            scr[y].insert(0,last_char)

        print(scr)


    elif "rotate column" in l:
        l = l.replace ("rotate column  ", "")















