liste=[]
count = 0
ergebnis=[]

file = open("Advent05.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(line.rstrip())
file.close()

#liste = ["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg","ieodomkazucvgmuy"]
#liste = ["hksifrqlsiqkzyex"]

def check_letterpair(string):
    for idx, char in enumerate(string):
        if idx == len(string)-2: return False
        temp_string = string[idx:idx+2]
        temp_start = temp_idx = idx+2
        while temp_idx < len(string):
            if temp_string == string[temp_idx:temp_idx+2]:
#                print(string)
                return True
            temp_idx += 1

for string in liste:
    if check_letterpair(string):
#        print(string)
        ergebnis.append(string)
        count += 1

ergebnis.sort()
for i in ergebnis:
    print(i)
print(count)














