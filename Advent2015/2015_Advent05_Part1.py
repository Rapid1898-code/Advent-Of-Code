liste=[]
count = 0


file = open("Advent05.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(line.rstrip())
file.close()

#liste = ["ugknbfddgicrmopn","aaa","jchzalrnumimnmhp","haegwjzuvuyypxyu","dvszwmarrgswjxmb"]

def check_vowels(string):
    temp_count = 0
    for char in string:
        if char in ["a","e","i","o","u"]: temp_count += 1
    if temp_count >= 3: return True
    else: return False

def check_twiceletter(string):
    for idx, char in enumerate(string):
        if idx == len(string)-1: return False
        if string[idx] == string[idx+1]: return True

def check_notstring(string):
    if "ab" in string: return False
    elif "cd" in string: return False
    elif "pq" in string: return False
    elif "xy" in string: return False
    else: return True

for string in liste:
    if check_vowels(string) and check_twiceletter(string) and check_notstring(string): count += 1

print(count)