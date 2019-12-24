liste = []
corners = {}
points1 = {}
points2 = {}
branches = {}
x = 0
y = 0
dir = ''
level = 0
paths = []
steps = 1
portal = ''
min_steps = 999999
temp_portals = []


def read_input():
    file = open("Advent20 Part1 Example03.txt", "r")
    for line in file:
        liste.append(line.rstrip('\n'))
    file.close()

def read_corners():
    corners['LUO'] = (2,2)
    corners['RUO'] = (len(liste[2])-1,2)
    corners['LDO'] = (2,len(liste)-1)
    corners['RDO'] = (len(liste[2])-1, len(liste)-1)

    for i in range(len(liste)-2):
        for j in range(len(liste[i])-2):
            if (liste[i][j].isalpha() or liste[i][j] == ' ') and j > 2 and i > 2:
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
    for j in range(len(liste[2])-4):
        if liste[0][j].isalpha():       # check highest line outside
            temp_string = liste[0][j] + liste[1][j]
            if temp_string not in points1: points1[temp_string] = (j,2,'D')
            else: points2[temp_string] = (j,2,'D')
        if liste[len(liste)-4][j].isalpha():        # check lowest line outside
            temp_string = liste[len(liste)-5][j] + liste[len(liste)-4][j]
            if temp_string not in points1: points1[temp_string] = (j, len(liste)-6, 'U')
            else: points2[temp_string] = (j, len(liste)-6, 'U')
        if liste[temp_line_innerup][j].isalpha() and j > 2 and j <= len(liste[2])-3:   # check highest line inside
            temp_string = liste[temp_line_innerup][j] + liste[temp_line_innerup+1][j]
            if temp_string not in points1: points1[temp_string] = (j,temp_line_innerup-1, 'U')
            else: points2[temp_string] = (j,temp_line_innerup-1, 'U')
        if liste[temp_line_innerdown][j].isalpha() and j > 2 and j <= len(liste[2])-3:   # check lowest line inside
            temp_string = liste[temp_line_innerdown-1][j] + liste[temp_line_innerdown][j]
            if temp_string not in points1: points1[temp_string] = (j,temp_line_innerdown+1, 'D')
            else: points2[temp_string] = (j,temp_line_innerdown+1, 'D')

    for j in range(len(liste)-5):
        if liste[j][0].isalpha() and j > 2 and j <= len(liste)-3:       # check left outside
            temp_string = liste[j][0:2]
            if temp_string not in points1: points1[temp_string] = (2,j,'R')
            else: points2[temp_string] = (2,j,'R')
        if liste[j][len(liste[2])-6].isalpha() and j > 2 and j <= len(liste) - 3:       # check right outside
            temp_string = liste[j][len(liste[2])-6] + liste[j][len(liste[2])-5]
            if temp_string not in points1: points1[temp_string] = (len(liste[2])-7,j,'L')
            else: points2[temp_string] = (len(liste[2])-7,j,'L')
        if liste[j][temp_line_innerleft].isalpha() and j > 2 and j <= len(liste) - 3:   # check left inside
            temp_string = liste[j][temp_line_innerleft] + liste[j][temp_line_innerleft+1]
            if temp_string not in points1: points1[temp_string] = (temp_line_innerleft-1,j,'L')
            else: points2[temp_string] = (temp_line_innerleft-1,j,'L')
        if liste[j][temp_line_innerright].isalpha() and j > 2 and j < len(liste) - 3:       # check right inside
            temp_string = liste[j][temp_line_innerright-1] + liste[j][temp_line_innerright]
            if temp_string not in points1: points1[temp_string] = (temp_line_innerright+1,j,'R')
            else: points2[temp_string] = (temp_line_innerright+1,j,'R')

def fillup():
    for i, s in enumerate(liste):
        for j in range(len(liste[2])+4 - len(s)):
            s += '#'
        liste[i] = s
    temp = ''
    for i in range(len(liste[2])+4):
        temp += '#'
    for i in range(3):
        liste.append(temp)

def check_point(act_dir):
    temp_directions = []
    if (liste[y][x + 1] == '.' and act_dir != 'L') or (liste[y][x + 1].isalpha() and steps > 1): temp_directions.append('R')
    if (liste[y][x - 1] == '.' and act_dir != 'R') or (liste[y][x - 1].isalpha() and steps > 1): temp_directions.append('L')
    if (liste[y + 1][x] == '.' and act_dir != 'U') or (liste[y + 1][x].isalpha() and steps > 1): temp_directions.append('D')
    if (liste[y - 1][x] == '.' and act_dir != 'D') or (liste[y - 1][x].isalpha() and steps > 1): temp_directions.append('U')
    return(temp_directions)

def go_direction(dir):
    global x,y
    if dir == 'R': x += 1
    elif dir == 'L': x -= 1
    elif dir == 'D': y += 1
    elif dir == 'U': y -= 1

read_input()                # read input file
read_corners()              # find corners of the field
print(corners)
fillup()                    # placeholder in form of # on right and down side
read_points()               # read all points aka teleports


x = points1['AA'][0]  # find start point
y = points1['AA'][1]
pos_directions = check_point('')
if len(pos_directions) == 1: paths.append([x,y,pos_directions[0],1])
else: print ('Error with Start Position')

print('Points1: ',points1)
print(len(points1))
print('Points2: ',points2)
print(len(points2))

while paths != []:
    x = paths[0][0]
    y = paths[0][1]
    dir = paths[0][2]
    steps = paths[0][3]
    pos_directions = ['X']
    while not liste[y][x].isalpha() and len(pos_directions) == 1:
        go_direction(dir)
        steps +=1
        pos_directions = check_point(dir)
        if len(pos_directions) == 1: dir = pos_directions[0]

    if len(pos_directions) > 1:
        for pos in pos_directions:
            paths.append([x,y,pos,steps])

    if liste[y][x].isalpha():
        if portal == 'AA': break

        if dir == 'D': portal = liste[y][x]+liste[y+1][x]
        if dir == 'U': portal = liste[y-1][x] + liste[y][x]
        if dir == 'R': portal = liste[y][x] + liste[y][x+1]
        if dir == 'L': portal = liste[y][x-1] + liste[y][x]

        if portal == 'ZZ':
            if steps < min_steps: min_steps = steps
        elif portal not in ('AA','ZZ'):
            print('Portal: ',portal)
            print('x:',x,'y:',y)
            addr1 = points1[portal]
            addr2 = points2[portal]
            if dir == 'D':
                if addr1[1] == y-1:
                    ziel = addr2
                    temp_portals.extend([portal, addr1,'-'])
                    temp_portals.extend([portal, addr2,'+'])
                else:
                    ziel = addr1
                    temp_portals.extend([portal, addr2,'-'])
                    temp_portals.extend([portal, addr1,'+'])
            if dir == 'U':
                if addr1[1] == y+1:
                    ziel = addr2
                    temp_portals.extend([portal, addr1,'-'])
                    temp_portals.extend([portal, addr2,'+'])
                else:
                    ziel = addr1
                    temp_portals.extend([portal, addr2,'-'])
                    temp_portals.extend([portal, addr1,'+'])
            if dir == 'R':
                if addr1[0] == x-1:
                    ziel = addr2
                    temp_portals.extend([portal, addr1,'-'])
                    temp_portals.extend([portal, addr2,'+'])
                else:
                    ziel = addr1
                    temp_portals.extend([portal, addr2,'-'])
                    temp_portals.extend([portal, addr1,'+'])
            if dir == 'L':
                if addr1[0] == x+1:
                    ziel = addr2
                    temp_portals.extend([portal, addr1,'-'])
                    temp_portals.extend([portal, addr2,'+'])
                else:
                    ziel = addr1
                    temp_portals.extend([portal, addr2,'-'])
                    temp_portals.extend([portal, addr1,'+'])
            paths.append ([ziel[0], ziel[1], ziel[2], steps])
    del paths[0]


print('Portal:',temp_portals)
print (paths)
print (min_steps-2)