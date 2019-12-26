import itertools

def format_input():
    file = open("Advent10Temp6.txt", "r")
    for line in file:
        liste.append(line.rstrip())
    file.close()

def asteroid_pos():
    for y in range (0, len(liste)):
        for x in range (0, len(liste[0])):
            if liste[y][x] == "#":
                asteroids_pos.append([x,y])
    asteroids_pos.sort()

def make_combi():
    liste = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    perm = itertools.product(liste, repeat=2)
    for i in perm:
        if i[0] == i[1] and i[0] != "1": continue
        if i[0] == "0" and i[1] != "1": continue
        if i[1] == "0" and i[0] != "1": continue
        combi.append([int(i[0]), int(i[1])])
    combi.sort()

def count_asteroids(x, y): # vorher zeile / spalte
    anz = 0
    blocker_gesamt = []
    tmp_blocker = []
    tmp_blockergesamt = []
    tmp_nodes = []

    for i in combi:

        tmp_x = x; tmp_y = y; zaehler_x = x; zaehler_y =y
        tmp_blocker.clear(); tmp_blockergesamt.clear()
        while tmp_x > 0 or tmp_y > 0:        # links oben
            if tmp_x > 0: tmp_x -= 1
            if tmp_y > 0: tmp_y -= 1
            zaehler_x = zaehler_x - i[0]
            zaehler_y = zaehler_y - i[1]
            # if [zaehler_x, zaehler_y] in asteroids_pos:
            tmp_blocker.append([zaehler_x, zaehler_y])
            tmp_blockergesamt.append([zaehler_x, zaehler_y])

        tmp_x = x; tmp_y = y; zaehler_x = x; zaehler_y =y
        tmp_blocker.clear()
        while tmp_x > 0 or tmp_y < len(liste)-1:        # links unten
            if tmp_x > 0: tmp_x -= 1
            if tmp_y < len(liste)-1: tmp_y += 1
            zaehler_x = zaehler_x - i[0]
            zaehler_y = zaehler_y + i[1]
            # if [zaehler_x, zaehler_y] in asteroids_pos:
            tmp_blocker.append([zaehler_x, zaehler_y])
            tmp_blockergesamt.append([zaehler_x, zaehler_y])

        tmp_x = x; tmp_y = y; zaehler_x = x; zaehler_y =y
        tmp_blocker.clear()
        while tmp_x < len(liste[0])-1 or tmp_y > 0:        # rechts oben
            if tmp_x < len(liste[0])-1: tmp_x += 1
            if tmp_y > 0: tmp_y -= 1
            zaehler_x = zaehler_x + i[0]
            zaehler_y = zaehler_y - i[1]
            # if [zaehler_x, zaehler_y] in asteroids_pos:
            tmp_blocker.append([zaehler_x, zaehler_y])
            tmp_blockergesamt.append([zaehler_x, zaehler_y])

        tmp_x = x; tmp_y = y; zaehler_x = x; zaehler_y =y
        tmp_blocker.clear()
        while tmp_x < len(liste[0])-1 or tmp_y < len(liste)-1:        # rechts unten
            if tmp_x < len(liste[0])-1: tmp_x += 1
            if tmp_y < len(liste)-1: tmp_y += 1
            zaehler_x = zaehler_x + i[0]
            zaehler_y = zaehler_y + i[1]
            #if [zaehler_x, zaehler_y] in asteroids_pos:
            tmp_blocker.append([zaehler_x, zaehler_y])
            tmp_blockergesamt.append([zaehler_x, zaehler_y])

        tmp_blockergesamt.sort()
        blocker_gesamt.append(list(tmp_blockergesamt))

    for i in asteroids_pos:     # Check für jeden Asterioden ob er für x,y sichtbar ist und gezählt werden kann
        sicht = True
        for j in blocker_gesamt:         # Prüfung für jede Kombination
            if i == [x,y]: sicht = False
            if i in j[1:] and i != [x,y]:       # Prüfunng wenn Quellpunkt und zu prüfender Asteroid (i) in der Kombination ist und Quellpunkt nicht gleich zu prüfender Asteroid
                for k in blocker_gesamt:
                    for l in k:
                        if l != [x,y] and l != j and l in asteroids_pos:
                            if x > l[0] > i[0] and y >= l[1] >= i[1]:
                                try:
                                    if (i[0] - x) / (i[1] - y) == (l[0] - x) / (l[1] - y):
                                        sicht = False
                                        # print('Check Asteroid: ', i[0], i[1])
                                        # print('Check Zwischenelement:', l[0], l[1])
                                        # print('Ausgangspunkt: ', x, y)
                                        # print('Blockerliste', j)
                                except:
                                    pass

                            if x < l[0] < i[0] and y > l[1] > i[1]:
                                try:
                                    if (i[0] - x) / (i[1] - y) == (l[0] - x) / (l[1] - y):
                                        sicht = False
                                        # print('Check Asteroid: ', i[0], i[1])
                                        # print('Check Zwischenelement:', l[0], l[1])
                                        # print('Ausgangspunkt: ', x, y)
                                        # print('Blockerliste', j)
                                except:
                                    pass
                            if x > l[0] > i[0] and y < l[1] < i[1]:
                                try:
                                    if (i[0] - x) / (i[1] - y) == (l[0] - x) / (l[1] - y):
                                        sicht = False
                                        # print('Check Asteroid: ', i[0], i[1])
                                        # print('Check Zwischenelement:', l[0], l[1])
                                        # print('Ausgangspunkt: ', x, y)
                                        # print('Blockerliste', j)
                                except:
                                    pass
                            if x < l[0] < i[0] and y <= l[1] <= i[1]:
                                try:
                                    if (i[0] - x) / (i[1] - y) == (l[0] - x) / (l[1] - y):
                                        sicht = False
                                        # print('Check Asteroid: ', i[0], i[1])
                                        # print('Check Zwischenelement:', l[0], l[1])
                                        # print('Ausgangspunkt: ', x, y)
                                        # print('Blockerliste', j)
                                except:
                                    pass
                            if x > l[0] > i[0] and y == l[1] == i[1]:
                                sicht = False
                                # print ('Check Asteroid: ', i[0], i[1])
                                # print ('Check Zwischenelement:', l[0], l[1])
                                # print ('Ausgangspunkt: ', x, y)
                                # print ('Blockerliste', j)
                            if x < l[0] < i[0] and y == l[1] == i[1]:
                                sicht = False
                                # print('Check Asteroid: ', i[0], i[1])
                                # print('Check Zwischenelement:', l[0], l[1])
                                # print('Ausgangspunkt: ', x, y)
                                # print('Blockerliste', j)
                            if x == l[0] == i[0] and y < l[1] < i[1]:
                                sicht = False
                                # print('Check Asteroid: ', i[0], i[1])
                                # print('Check Zwischenelement:', l[0], l[1])
                                # print('Ausgangspunkt: ', x, y)
                                # print('Blockerliste', j)
                            if x == l[0] == i[0] and y > l[1] > i[1]:
                                sicht = False
                                # print('Check Asteroid: ', i[0], i[1])
                                # print('Check Zwischenelement:', l[0], l[1])
                                # print('Ausgangspunkt: ', x, y)
                                # print('Blockerliste', j)

        if sicht == True:
            anz += 1
            tmp_nodes.append(i)

    print('X: ',x, 'Y: ',y, 'Anz: ',anz)
    print(tmp_nodes)
    return (anz)

liste = []
max_asteroids = 0
max_coordinates =[]
asteroids_pos = []
combi = []

format_input()
asteroid_pos()
make_combi()

# gesamtanzahl = count_asteroids(3,4)

for i in asteroids_pos:
    gesamtanzahl = count_asteroids(i[0],i[1])         # Anzahl der direkten Asteroiden ermitteln#
    if gesamtanzahl > max_asteroids:
        max_asteroids = gesamtanzahl
        max_coordinates = [i[0],i[1]]
print(max_asteroids)
print(max_coordinates)
