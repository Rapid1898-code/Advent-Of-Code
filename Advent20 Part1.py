liste = []
corners = {}
points1 = {}
points2 = {}
branches = {}
x = 0
y = 0
dir = ''

def read_input():
    file = open("Advent20 Part1 Example02.txt", "r")
    for line in file:
        liste.append(line.rstrip())
    file.close()

def read_corners():
    corners['LUO'] = (2,2)
    corners['RUO'] = (len(liste[2])-1,2)
    corners['LDO'] = (2,len(liste)-1)
    corners['RDO'] = (len(liste[2])-1, len(liste)-1)

    for i in range(len(liste)-1):
        for j in range(len(liste[i])-1):
            if (liste[i][j].isalpha() or liste[i][j] == ' ') and j > 2 and i >2:
                corners['LUI'] = (j, i)
                temp_x = j
                while liste[i][temp_x] != '#' and liste[i][temp_x] != '.':
                    temp_x += 1
                corners['RUI'] = (temp_x-1,i)
                temp_y = i
                while liste[temp_y][j].isalpha() or liste[temp_y][j] == ' ':
                    temp_y += 1
                corners['LDI'] = (j,temp_y-1)
                corners['RDI'] = (temp_x-1,temp_y-1)
                return()

def read_points():
    temp_line_innerup = corners['LUI'][1]
    temp_line_innerdown = corners['LDI'][1]
    temp_line_innerleft = corners['LUI'][0]
    temp_line_innerright = corners['RDI'][0]
    for j in range(len(liste[2])+2):
        try:
            if liste[0][j].isalpha():       # check highest line outside
                temp_string = liste[0][j] + liste[1][j]
                if temp_string not in points1: points1[temp_string] = (j,2)
                else: points2[temp_string] = (j,2)
        except: pass
        try:
            if liste[len(liste)-2][j].isalpha():        # check lowest line outside
                temp_string = liste[len(liste)-2][j] + liste[len(liste)-1][j]
                if temp_string not in points1: points1[temp_string] = (j, len(liste)-3)
                else: points2[temp_string] = (j, len(liste)-3)
        except: pass
        try:
            if liste[temp_line_innerup][j].isalpha() and j > 2 and j <= len(liste[2])-3:   # check highest line inside
                temp_string = liste[temp_line_innerup][j] + liste[temp_line_innerup+1][j]
                if temp_string not in points1: points1[temp_string] = (j,temp_line_innerup-1)
                else: points2[temp_string] = (j,temp_line_innerup-1)
        except: pass
        try:
            if liste[temp_line_innerdown][j].isalpha() and j > 2 and j <= len(liste[2])-3:   # check lowest line inside
                temp_string = liste[temp_line_innerdown-1][j] + liste[temp_line_innerdown][j]
                if temp_string not in points1: points1[temp_string] = (j,temp_line_innerdown+1)
                else: points2[temp_string] = (j,temp_line_innerdown+1)
        except: pass

    for j in range(len(liste)):
        try:
            if liste[j][0].isalpha() and j > 2 and j <= len(liste)-3:       # check left outside
                temp_string = liste[j][0:2]
                if temp_string not in points1: points1[temp_string] = (2,j)
                else: points2[temp_string] = (2,j)
        except: pass
        try:
            if liste[j][len(liste[2])+1].isalpha() and j > 2 and j <= len(liste) - 3:       # check right outside
                temp_string = liste[j][len(liste[2])] + liste[j][len(liste[2])+1]
                if temp_string not in points1: points1[temp_string] = (len(liste[2])-1,j)
                else: points2[temp_string] = (len(liste[2])-1,j)
        except: pass
        try:
            if liste[j][temp_line_innerleft].isalpha() and j > 2 and j <= len(liste) - 3:   # check left inside
                temp_string = liste[j][temp_line_innerleft] + liste[j][temp_line_innerleft+1]
                if temp_string not in points1: points1[temp_string] = (temp_line_innerleft-1,j)
                else: points2[temp_string] = (temp_line_innerleft-1,j)
        except: pass
        try:
            if liste[j][temp_line_innerright].isalpha() and j > 2 and j < len(liste) - 3:       # check right inside
                temp_string = liste[j][temp_line_innerright-1] + liste[j][temp_line_innerright]
                if temp_string not in points1: points1[temp_string] = (temp_line_innerright+1,j)
                else: points2[temp_string] = (temp_line_innerright+1,j)
        except: pass

def read_startpos():
    if y == 2 or y == corners['LDI'][1]+1: dir='D'
    elif y == len(liste)-3 or y == corners['LUI'][1] -1: dir='U'
    elif x == 2 or x == corners['RDI'][0]: dir='R'
    elif x == len(liste[2]) or x == corners['LUI'][0]: dir='L'
    else: print("Error Read Startpos ", x,y)

def check_point():
    temp_directions = []
    if liste[y][x + 1] == '.': temp_directions.append('R')
    if liste[y][x - 1] == '.': temp_directions.append('L')
    if liste[y + 1][x] == '.': temp_directions.append('D')
    if liste[y - 1][x] == '.': temp_directions.append('U')
    return(temp_directions)

def go_direction(dirs):
    if dirs == 1:
        if dirs[0] == 'R': x += 1
        elif dirs[0] == 'L': x -= 1
        elif dirs[0] == 'D': y += 1
        elif dirs[0] == 'U': y -= 1
    else:
        pass


read_input()                # read input file
read_corners()              # find corners of the field
read_points()               # read all points aka teleports
x = points1['AA'][0]  # find start point
y = points1['AA'][1]
read_startpos()


#
# while True:
#     pos_directions = check_point()
#     if len(pos_directions) > 1:
#         branches.append[(x,y)] = pos_directions
#         go_direction(pos_directions)
#     else:
#         go_direction(pos_directions)




# print('Liste: ',liste)
# print('Corners: ',corners)
print('Points1: ',points1)
print('Points2: ',points2)