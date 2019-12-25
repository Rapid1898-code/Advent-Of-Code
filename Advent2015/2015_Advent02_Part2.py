liste = []; presents = []
length = 0; width = 0; height = 0; square_feet = 0; ribbon_feet = 0
file = open("Advent02.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(line.rstrip())
file.close()

def read_input():
    for eintrag in liste:
        for lfdnr, char in enumerate (eintrag):
            if char == 'x':
                length = int(eintrag[:lfdnr])
                tmp_eintrag = eintrag[lfdnr+1:]
                break
        for lfdnr, char in enumerate (tmp_eintrag):
            if char == 'x':
                width = tmp_eintrag[:lfdnr]
                height = tmp_eintrag[lfdnr+1:]
        presents.append([int(length), int(width), int(height)])

read_input()
for present in presents:
    temp_paper = 2*present[0]*present[1] + 2*present[1]*present[2] + 2*present[2]*present[0]
    temp_paper_extra = min(present[0]*present[1], present[1]*present[2], present[2]*present[0])
    temp_paper_ges = temp_paper + temp_paper_extra
    square_feet += temp_paper_ges

    temp_ribbon = 2*present[0] + 2*present[1] + 2*present[2] - 2*(max(present))
    temp_ribbon_bow = present[0] * present[1] * present[2]
    temp_ribbon_ges = temp_ribbon + temp_ribbon_bow
    ribbon_feet += temp_ribbon_ges
    print(temp_ribbon, temp_ribbon_bow, temp_ribbon_ges)


#print(presents)
print("Paper: ", square_feet)
print("Ribbon ", ribbon_feet)



