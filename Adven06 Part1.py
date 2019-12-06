liste = []
summe = 0
dict_erg = {}

file = open("Advent06.txt", "r")
for line in file:
    w1 = line.rstrip()[:3]
    w2 = line.rstrip()[4:]
    liste.append([w1,w2])
file.close()


suche=['COM']
suchtemp = []

while suche != []:
    for i in suche:
        for j in liste:
            if j[0] == i:
                suchtemp.append(j[1])
                if i in dict_erg:
                    wert = int(dict_erg.get(i)[1]) + 1
                else:
                    wert = 0
                dict_erg[j[1]] = [1,wert]
    suche = suchtemp
    suchtemp = []

for key, value in dict_erg.items():
    summe += value[0] + value[1]

print (dict_erg)
print (summe)
