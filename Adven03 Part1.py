import csv

def readlist (filename):
    file = open(filename, "r")
    csv_reader = csv.reader(file, delimiter=",")
    liste = list(csv_reader)
    liste = [row[0] for row in liste]
    return (liste)

def read_direction (code):
    return(code[:1])

def read_steps (code):
    return(int(code[1:]))

def fill_vektors (liste):
    mat = []
    x = 0
    y = 0
    for i in liste:
        node = []
        direction = read_direction(i)
        steps = read_steps(i)
        if direction in ('R','L'):
            node.append('H')
        elif direction in ('D','U'):
            node.append('V')
        else:
            return "Falsche Direction!"
        node.append(x)
        node.append(y)
        if direction == 'R': x += steps
        if direction == 'L': x -= steps
        if direction == 'U': y += steps
        if direction == 'D': y -= steps
        node.append(x)
        node.append(y)
        mat.append(node)
    return mat

def vektor_sort(vektor):
    output_h = []
    output_v = []
    for i in vektor:
        if i[0] == 'H':
            output_h.append(i)
        elif i[0] == 'V':
            output_v.append(i)
        else:
            return ('Fehler - Falscher Buchstabe not H or V')
    return output_h, output_v

matrix1 = []
matrix2 = []

liste1 = readlist("Advent03_liste1.csv")
liste2 = readlist("Advent03_liste2.csv")
vektor1 = fill_vektors(liste1)
vektor2 = fill_vektors(liste2)

list1_h, list1_v=vektor_sort(vektor1)
list2_h, list2_v=vektor_sort(vektor2)

ergebnis_list=[]
ergebnis=1000000
for i in list1_h:
    for j in list2_v:
        if i[1] <= j[1] <= i[3] and j[4] <= i[2] <= j[2]:
            ergebnis_list.append([i[2], j[1]])
            if i[2] + j[1] < ergebnis:
                ergebnis = abs(i[2]) + abs(j[1])
for i in list2_h:
    for j in list1_v:
        if i[1] <= j[1] <= i[3] and j[4] <= i[2] <= j[2]:
            ergebnis_list.append([i[2], j[1]])
            if i[2] + j[1] < ergebnis:
                ergebnis = abs(i[2]) + abs(j[1])

print(ergebnis_list)
print(ergebnis)


























