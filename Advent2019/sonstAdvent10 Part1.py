import itertools

liste = []
max_asteroids = 0
asteroids_pos = []
width = 0
heigth = 0

def format_input():
    file = open("Advent10Temp6.txt", "r")
    for line in file:
        liste.append(line.rstrip())
    file.close()

def make_combi(liste):
    perm = itertools.product(liste, repeat=2)
    combi = []
    for i in perm:
        if i[0] == i[1] and i[0] != "1": continue
        if i[0] == "0" and i[1] != "1": continue
        if i[1] == "0" and i[0] != "1": continue
        combi.append([int(i[0]), int(i[1])])
    return(combi)

def check_directsight(x,y, source_x, source_y):
    a=0
    for i in asteroids_pos:
        if x == source_x and y == source_y: return False            # check if source and check-target the same coordinate
        if x == source_x and x == i[0]:         # Prüfung senk und waagrecht
            if i[1] > y and i[1] < source_y: return False
            if i[1] < y and i[1] > source_y: return False
        if y == source_y and y == i[1]:
            if i[0] > x and i[0] < source_x: return False
            if i[0] < x and i[0] > source_x: return False
        if abs(x-source_x) == abs(y-source_y) and abs(x-i[0]) == abs(y-i[1]):       # Prüfung der Diagonalen
                if i[1] > source_y and i[1] < y:
                    if i[0] < x and i[0] > source_x: return False
                    if i[0] > x and i[0] < source_x: return False
                if i[1] < source_y and i[1] > y:
                    if i[0] < x and i[0] > source_x: return False
                    if i[0] > x and i[0] < source_x: return False

        # if x > source_x and y > source_y:       # right / down corner
        maxi = 0
        maxi = max(abs(x-source_x), abs(y-source_y))
        temp_liste = []
        for m in range(0,maxi+1): temp_liste.append(m)
        temp_combi = make_combi(temp_liste)

        for j in temp_combi:
            if (x==0 and source_x==0) or (y==0 and source_y==0): continue
            if x > (source_x+j[0]) > source_x and y > (source_y+j[1]) > source_y:
                try:
                    if ((source_x+j[0]-source_x)/(source_y+j[1]-source_y)) == ((x-source_x) / (y-source_y)) and [j[0]+source_x,j[1]+source_y] in asteroids_pos:
                        a=0
                        return False
                except:
                    pass
            elif x > (source_x+j[0]) > source_x and y < (y+j[1]) < source_y:     # right / upper corner
                try:
                    if ((source_x+j[0]-source_x)/(y+j[1]-source_y)) == ((x-source_x) / (y-source_y)) and [j[0]+source_x,j[1]+y] in asteroids_pos:
                        a=0
                        return False
                except:
                    pass
            elif x < (x+j[0]) < source_x and y > (source_y+j[1]) >source_y:     # left / down corner
                try:
                    if ((x+j[0]-source_x)/(source_y+j[1]-source_y)) == ((x-source_x) / (y-source_y)) and [j[0]+x,j[1]+source_y] in asteroids_pos:
                        a = 0
                        return False
                except:
                    pass
            elif x < (x+j[0]) < source_x and y < (y+j[1]) < source_y:     # left / uppper corner
                try:
                    if ((x+j[0]-source_x)/(y+j[1]-source_y)) == ((x-source_x) / (y-source_y)) and [j[0]+x,j[1]+y] in asteroids_pos:
                        a = 0
                        return False
                except:
                    pass



    return True

def count_asteroids(x, y): # vorher zeile / spalte
    anz = 0
    # print ('x:', x, 'y: ',y)
    # Check waggrecht - rechts und links
    temp_nodes = []
    for i in asteroids_pos:
        if x==i[0] and y==i[1]: continue
        elif check_directsight(i[0],i[1],x,y):
            anz += 1
            temp_nodes.append([i[0],i[1]])
    print ('X:', x, 'Y:', y, 'Erg: ', anz)
    print(temp_nodes)
    return(anz)

format_input()      # Ermittlung aller Positionen x,y wo Asteroiden sind
for y in range (0, len(liste)):
    for x in range (0, len(liste[0])):
        if liste[y][x] == "#":
            asteroids_pos.append([x,y])
width = len(liste[0])
heigth = len(liste)

for i in asteroids_pos:     # für jeden einzelnen Asteroiden
    anzahl = count_asteroids(i[0],i[1])         # Anzahl der direkten Asteroiden ermitteln
    if anzahl > max_asteroids:
        max_asteroids = anzahl
        best = i

print ('Ergebnis: ', max_asteroids)
print ('X: ', best[0], 'Y: ',best[1])