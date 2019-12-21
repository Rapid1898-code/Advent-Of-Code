liste_src = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

#liste_src = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
#liste_src =[3,8,1001,8,10,8,105,1,0,0,21,34,51,64,81,102,183,264,345,426,99999,3,9,102,2,9,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,1002,9,5,9,4,9,99,3,9,102,3,9,9,101,3,9,9,1002,9,4,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,5,9,101,3,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

import itertools

# erstellt Liste mit allen Kombinationsmöglichkeiten des Parameters und stellt sie in eine Liste
def make_combi(numb):
    combi2 = []
    combi = itertools.permutations(numb, len(numb))
    for i in combi:
        combi2.append(i)
    return combi2

# 2 Zahlen addieren lt. Position
def op_add():
    global i
    liste[liste[i + 3]] = liste[liste[i + 1]] + liste[liste[i + 2]]
    i += 4

# 2 Zahlen multiplizieren lt. Position
def op_mult():
    global i
    liste[liste[i + 3]] = liste[liste[i + 1]] * liste[liste[i + 2]]
    i += 4

# Eingabe eines Wertes lt. Position
# bei 0 erfolgt Eingabe lt. Position
# bei 1 erfolgt Eingabe direkt für die akt. Position
# bei I1 wird der Code lt. Position geschrieben
# bei I2 wird der Code lt. Position geschrieben
def op_in(inst, code):
    global i
    if inst == '0':     # Abfrage für manuelle Eingabe im Positionsmode (alte Logik)
        inp = input("Input: ")
        liste[liste[i + 1]] = int(inp)
    elif inst == '1':   # Abfrage für manuelle Eingabe im Direktmode (alte Logik
        inp = input("Input: ")
        liste[i + 1] = int(inp)
    elif inst == "I": liste[liste[i + 1]] = code
    else: print('Error F! ', inst)
    i += 2

# Ausgabe bei return eines Wertes aus der Funktion
# bei 0 erfolgt Ausgabe lt. Position
# bei 1 erfolgt Ausgabe direkt für die akt. Position
def op_out(inst):
    global i
#    if inst == '0': print("Output: ", liste[liste[i + 1]]) => was necessary for Advent5
#    elif inst == '1': print("Output: ", liste[i + 1])
    if inst == '0': return(liste[liste[i + 1]])
    elif inst == '1': return(liste[i + 1])
    else: print ('Error D! ', inst)
    i += 2

# Vergleich ob der Wert <> 0 ist
# Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# Parameter2 gib an ob die Prüfung <> 0 lt. Position (0) oder direktem Wert (1) erfolgen soll
def op_true(in1, in2):
    global i
    if in2 == '0':
        if liste[liste[i+1]] != 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            else:
                i = liste[i + 2]
        else:
            i += 3
    else:
        if liste[i + 1] != 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            else:
                i = liste[i + 2]
        else:
            i += 3

# Vergleich ob der Wert = 0 ist
# Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# Parameter2 gib an ob die Prüfung = 0 lt. Position (0) oder direktem Wert (1) erfolgen soll
def op_false(in1, in2):
    global i
    if in2 == '0':
        if liste[liste[i+1]] == 0:
            if in1 == '0':
                i = liste[liste[i+2]]
            else:
                i = liste[i+2]
        else:
            i += 3
    else:
        if liste[i+1] == 0:
            if in1 == '0':
                i = liste[liste[i+2]]
            else:
                i = liste[i+2]
        else:
            i += 3

# 2 Werte werden verglichen - wenn < wird 1 ausgegeben - sonst 0
# # Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# # Parameter2 gib an ob die Prüfung lt. Position (0) oder direktem Wert (1) erfolgen soll
def op_less(in1, in2):
    global i
    if in2 == '0':
        v1 = liste[liste[i + 1]]
    else:
        v1 = liste[i + 1]
    if in1 == '0':
        v2 = liste[liste[i + 2]]
    else:
        v2 = liste[i + 2]
    if v1 < v2:
        liste[liste[i + 3]] = 1
    elif v1 >= v2:
        liste[liste[i + 3]] = 0
    i += 4

# 2 Werte werden verglichen - wenn = wird 1 ausgegeben - sonst 0
# # Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# # Parameter2 gib an ob die Prüfung lt. Position (0) oder direktem Wert (1) erfolgen soll
def op_equal(in1, in2):
    global i
    if in2 == '0':
        v1 = liste[liste[i+1]]
    else:
        v1 = liste[i+1]
    if in1 == '0':
        v2 = liste[liste[i + 2]]
    else:
        v2 = liste[i+2]
    if v1 == v2:
        liste[liste[i + 3]] = 1
    elif v1 != v2:
        liste[liste[i + 3]] = 0
    i += 4

def val_instruct(in1, in2):
    global i
    if in2 == '0':
        v1 = liste[liste[i + 1]]
    elif in2 == '1':
        v1 = liste[i + 1]
    else:
        print("ErrorA! ", in2)
    if in1 == '0':
        v2 = liste[liste[i + 2]]
    elif in1 == '1':
        v2 = liste[i + 2]
    else:
        print("ErrorB! ", in1)
    return v1, v2

# Eigentlichs Herzstück des Int-Computers
# bei optout wird ergebnis der Funktion zurückgegeben
def int_comp(code1,code2):
    global i
    global inp_inst
    global loop
    while True:
        if liste[i] == 99:
            loop = False
            return (code2)
        if liste[i] == 1:
            op_add()
            continue
        if liste[i] == 2:
            op_mult()
            continue
        if liste[i] == 3:
            if inp_inst == 0:
                inp_inst += 1
                op_in('I',code1)    # bei der ersten Ansteuerung des Amplifiers wird der Initialwert aus dem 5-stelligen Code genommen
            elif inp_inst == 1:
                op_in('I',code2)    # ab dem 2.Lauf wird immer der aktuelle Out-Wert (=Out-Wert des letzten Amplifier) genommen
            else:
                op_in('0',0)
            continue
        if liste[i] == 4:
            erg = op_out('0')
            i += 2
            return (erg)
        if liste[i] == 5:
            op_true('0', '0')
            continue
        if liste[i] == 6:
            op_false('0', '0')
            continue
        if liste[i] == 7:
            op_less('0','0')
            continue
        if liste[i] == 8:
            op_equal('0','0')
            continue

        if liste[i] > 4:
            instruct = str(liste[i])
            while len(instruct) < 5: instruct = '0' + instruct
            opcode = instruct[3:]

            if opcode == '01':
                value1, value2 = val_instruct(instruct[1], instruct[2])
                liste[liste[i + 3]] = value1 + value2
                i += 4
            elif opcode == '02':
                value1, value2 = val_instruct(instruct[1], instruct[2])
                liste[liste[i + 3]] = value1 * value2
                i += 4
            elif opcode == '03':
                op_in(instruct[2])
            elif opcode == '04':
                erg=op_out(instruct[2])
                return (erg)
            elif opcode == '05':
                op_true(instruct[1],instruct[2])
            elif opcode == '06':
                op_false(instruct[1],instruct[2])
            elif opcode == '07':
                op_less(instruct[1],instruct[2])
            elif opcode == '08':
                op_equal(instruct[1],instruct[2])
            else: print ("Error E ", opcode)


combi = make_combi('56789')
# test = ('9', '8', '7', '6', '5')
# test2 = []
# test2.append(test)
# print (test2)
# combi = list(test2)
ergebnis = 0

for a in combi:
    out = 0
    ind_AbisE = []
    li_AbisE = []
    loop = True
    for b in a:     # Initialer Start der Amplifier mit Startwert
        i=0
        inp_inst = 0        # Abfrge wg. Initialisierung der Amplifier
        liste = liste_src
        out=int_comp(int(b),out)
        ind_AbisE.append(i)     # Liste mit Indizes der einzelnen Amplifiers
        li_AbisE.append(list(liste))  # Liste mit den aktuellen Werten der einzelnen Amplifiers
#        print ('Amp:', len(ind_AbisE), 'Index:', i, 'Out:', out, 'Liste:', liste)

    amp=0
    while loop:     # Laufender Betrieb der Amplifier mit Output von vorherigem Amplifier bis Ende mit 99 erreicht bei Amplifier E
        i=ind_AbisE[amp]
        liste=list(li_AbisE[amp])
        out=int_comp(int(a[amp]),out)
        ind_AbisE[amp]=i
        li_AbisE[amp]=list(liste)
#        print('Amp:', amp+1, 'Index:', i, 'Out:', out, 'Liste:', liste)

        if loop == False and amp == 4:
            break
        else:
            loop = True
        ind_AbisE[amp] = i
        li_AbisE[amp] = list(liste)
        if amp == 4:
            amp = 0
        else:
            amp += 1

    if out > ergebnis:
        ergebnis = out
        ergebnis_combi = a

print (ergebnis)
print (ergebnis_combi)

















