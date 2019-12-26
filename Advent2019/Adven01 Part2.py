liste = []  # Liste für Elemente initialisieren
summe = 0   # Gesamtsumme initialsiieren

file = open("Advent01.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(int(line))
file.close()

for i in liste:
    calc = i // 3 - 2
    while calc > 0:
        summe = summe + calc
        calc = calc // 3 - 2

print("Endsumme: ", summe)