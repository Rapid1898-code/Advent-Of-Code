liste = []

def read_input():
    file = open("Advent20 Part1 Example01.txt", "r")
    for line in file:
        liste.append(line.rstrip('\n'))
    file.close()

read_input()
for i in liste:
    print (len(i))