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
    step_sum = 0
    for i in liste:
        node = []
        direction = read_direction(i)
        steps = read_steps(i)
        step_sum += steps
        if direction in ('R','L'):
            node.append('H')
        elif direction in ('D','U'):
            node.append('V')
        else:
            return "Falsche Direction!"
        if direction == 'R': x += steps
        if direction == 'L': x -= steps
        if direction == 'U': y += steps
        if direction == 'D': y -= steps
        node.append(x)
        node.append(y)
        node.append(step_sum)
        node.append(direction)
        node.append(steps)
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

#read input
liste1 = readlist("Advent03_liste1.csv")
liste2 = readlist("Advent03_liste2.csv")
#build vektors for both inputs with number of steps
vektor1 = fill_vektors(liste1)
vektor2 = fill_vektors(liste2)
#split vektors to horizonal and vertical
list1_h, list1_v=vektor_sort(vektor1)
list2_h, list2_v=vektor_sort(vektor2)

#print(liste1)
#print(vektor1)
#print(liste2)
#print(vektor2)
print(list1_h)
print(list2_v)

#check intersections and least amount of steps
ergebnis_list=[]
ergebnis=1000000
# v / x-Ende / y-Ende / Summe Steps / Direction / Step
for i in list1_h:
    for j in list2_v:
        if i[4]=='R' and not (i[1]-i[5] < j[1] < i[1]): continue
        if i[4]=='L' and not (i[1] < j[1] < i[1]+i[5]): continue
        if j[4]=='D' and not (j[2] < i[2] < j[2]+j[5]): continue
        if j[4]=='U' and not (j[2]-j[5] < i[2] < j[2]): continue
        ergebnis_list.append([j[1], i[2]])
        temp = i[3] + j[3] - abs(j[1] - i[1]) - abs(j[2] - i[2])
        if temp < ergebnis: ergebnis = temp

for i in list2_h:
    for j in list1_v:
        if i[4]=='R' and not (i[1]-i[5] < j[1] < i[1]): continue
        if i[4]=='L' and not (i[1] < j[1] < i[1]+i[5]): continue
        if j[4]=='D' and not (j[2] < i[2] < j[2]+j[5]): continue
        if j[4]=='U' and not (j[2]-j[5] < i[2] < j[2]): continue
        ergebnis_list.append([j[1],i[2]])
        temp = i[3]+j[3] - abs(j[1]-i[1]) - abs(j[2]-i[2])
        if temp < ergebnis: ergebnis = temp

print(ergebnis_list)
print(ergebnis)


























