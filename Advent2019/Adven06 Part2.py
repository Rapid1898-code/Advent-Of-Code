liste = []
summe = 0
dict_erg = {}

file = open("Advent06.txt", "r")
for line in file:
    w1 = line.rstrip()[:3]
    w2 = line.rstrip()[4:]
    liste.append([w1,w2])
file.close()

you = ['YOU']
while you[-1] != 'COM':
    for i in liste:
        if i[1] == you[-1]:
            you.append(i[0])

san = ['SAN']
while san[-1] != 'COM':
    for i in liste:
        if i[1] == san[-1]:
            san.append(i[0])

short = 100000
for i in range (0, len(you)-1):
    for j in range (0, len(san)-1):
        if you[i] == san[j]:
            if (i-1 + j-1) < short:
                short = (i-1 + j-1)

print (short)

