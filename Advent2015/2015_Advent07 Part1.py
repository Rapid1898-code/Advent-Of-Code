with open('Advent07Input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
index = [l.split() for l in lines]
ergebnis = []
print(len(index))

def bit_not(n, numbits=16):
    return (1 << numbits) - 1 - n

while index != []:
    temp_del = []
    for idx,value in enumerate(index):
        if value[2] == "a" and value[0] in ergebnis:
            temp_calc = ergebnis[ergebnis.index(value[0])+1]
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[1] == "AND" and value[0] in ergebnis and value[2] in ergebnis:
            temp_calc = ergebnis[ergebnis.index(value[0])+1] & ergebnis[ergebnis.index(value[2])+1]
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[0].isdigit() and value[1] == "AND" and value[2] in ergebnis:
            temp_calc = 1 & ergebnis[ergebnis.index(value[2])+1]
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[1] == "OR" and value[0] in ergebnis and value[2] in ergebnis:
            temp_calc = ergebnis[ergebnis.index(value[0])+1] | ergebnis[ergebnis.index(value[2])+1]
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[1] == "LSHIFT" and value[0] in ergebnis:
            temp_calc = ergebnis[ergebnis.index(value[0])+1] << int(value[2])
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[1] == "RSHIFT" and value[0] in ergebnis:
            temp_calc = ergebnis[ergebnis.index(value[0])+1] >> int(value[2])
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[0] == "NOT" and value[1] in ergebnis:
            temp_calc = bit_not (ergebnis[ergebnis.index(value[1])+1])
            ergebnis.extend ([value[-1], temp_calc])
            temp_del.append (idx)
        if value[0].isdigit() and value[1] == '->':
            ergebnis.extend([value[-1], int(value[0])])
            temp_del.append(idx)

    temp_del.sort(reverse=True)
    for temp_idx in temp_del:
        del index[temp_idx]

print(ergebnis)
print(len(index))
print(ergebnis[ergebnis.index("a")+1])




