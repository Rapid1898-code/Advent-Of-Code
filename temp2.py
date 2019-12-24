liste = []

def read_input():
    file = open("Advent20 Part1 Example01.txt", "r")
    for line in file:
        liste.append(line.rstrip())
    file.close()
    for i, s in enumerate(liste):
        for j in range(len(liste[2])+4 - len(s)):
            s += '#'
        liste[i] = s
    temp = ''
    for i in range(len(liste[2])+4):
        temp += '#'
    for i in range(3):
        liste.append(temp)


read_input()
for i in liste:
    print (len(i), i)