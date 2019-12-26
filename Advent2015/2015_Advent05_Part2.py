liste=[]
count = 0


file = open("Advent05.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(line.rstrip())
file.close()

liste = ["qjhvhtzxzqqjkmpb","xxyxx","uurcxstgmygtbstg",""]

def check_letterbetween(string):
    for idx2, char2 in enumerate(string):
        if idx2 == len(string)-3: return False
        if string[idx2] == string[idx2+2]: return True

def check_letterpair(string):
    for idx, char in enumerate(string):
        if idx == len(string)-2: return False
        temp_string = string[idx:idx+2]
        temp_start = temp_idx = idx+2
        while temp_idx < len(string):
            if temp_string == string[temp_idx:temp_idx+2]:
                if check_letterbetween(string[temp_start:temp_idx]) == True: return True
            temp_idx += 1

for string in liste:
    if check_letterpair(string): count += 1

print(count)