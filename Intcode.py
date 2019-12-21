import itertools

# erstellt Liste mit allen Kombinationsmöglichkeiten des Parameters und stellt sie in eine Liste
def make_combi(numb):
    combi2 = []
    combi = itertools.permutations(numb, len(numb))
    for i in combi:
        combi2.append(i)
    return combi2

# Initialisiert die Liste mit x bis zum Maximalwert
def memory_extend(list_extend_index):
    for j in range(list_extend_index - len(liste) + 2):
        liste.append(0)

# Prüft ob ein Werte über die Grenze der Liste hinausgeht
def memory_check (instruct, werte):
    global i
    max = 0
    for j in range (0,len(werte)):
        if (instruct[j] == '0' or instruct[j] == '2') and werte[j] > max: max = werte[j]
    if max > len(liste): memory_extend(int(max))

# OPCODE 1
def op_add(erg, wert1, wert2):
    global i
    try:
        liste[erg] = wert1 + wert2
    except:
        memory_extend(liste[erg])
        liste[erg] = wert1 + wert2
    i += 4

# 2 Zahlen multiplizieren lt. Position
# OPCODE 2
def op_mult(erg, wert1, wert2):
    global i
    try:
        liste[erg] = wert1 * wert2
    except:
        memory_extend(liste[erg])
        liste[erg] = wert1 * wert2
    i += 4

# Eingabe eines Wertes lt. Position
# bei 0 erfolgt Eingabe lt. Position
# bei 1 erfolgt Eingabe direkt für die akt. Position
# bei I1 wird der Code lt. Position geschrieben
# bei I2 wird der Code lt. Position geschrieben
# OPCODE 3
def op_in(inst, code):
    global i
    global relative_base
    global mode, x, y
    if inst == '0':     # Abfrage für manuelle Eingabe im Positionsmode (alte Logik)
        inp = input("Input: ")
        liste[liste[i + 1]] = int(inp)
    elif inst == '1':   # Abfrage für manuelle Eingabe im Direktmode (alte Logik
        inp = input("Input: ")
        liste[i + 1] = int(inp)
    elif inst == '2':
        inp = input("Input: ")
        liste[liste[i + 1]+relative_base] = int(inp)
    elif inst == "I": liste[liste[i + 1]] = code
    else: print('Error F! ', inst)
    i += 2

# Ausgabe bei return eines Wertes aus der Funktion
# bei 0 erfolgt Ausgabe lt. Position
# bei 1 erfolgt Ausgabe direkt für die akt. Position
# OPCODE 4
def op_out(inst):
    global i, mode, relative_base, robo_color, robo_dir
    if mode == 'LOOP':
        if inst == '0':
            return (liste[liste[i + 1]])
        elif inst == '1':
            return (liste[i + 1])
        elif inst == '2':
            return (liste[liste[i + 1]+relative_base])
    elif mode == 'TEST':
        if inst == '0': print("Output: ", liste[liste[i + 1]])      # was necessary for Advent5
        elif inst == '1': print("Output: ", liste[i + 1])
        elif inst == '2': print("Output: ", liste[liste[i + 1]+relative_base])
    elif mode == 'ROBOT':
        if inst == '0': robo_move(liste[liste[i + 1]])
        elif inst == '1': robo_move(liste[i + 1])
        elif inst == '2': robo_move(liste[liste[i + 1]+relative_base])
    else: print ('Error D! ', inst)
    i += 2

# Vergleich ob der Wert <> 0 ist
# Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# Parameter2 gib an ob die Prüfung <> 0 lt. Position (0) oder direktem Wert (1) erfolgen soll
# OPCODE 5
def op_true(in1, in2):      # in2 ist der erste Parameter nach dem Operanden - in1 ist der zweite parameter nach dem Operanden
    global i
    global relative_base
    if in2 == '0':
        if liste[liste[i+1]] != 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2]+relative_base]
        else:
            i += 3
    elif in2 == '1':
        if liste[i + 1] != 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2]+ relative_base]
        else:
            i += 3
    elif in2 == '2':
        if liste[liste[i+1]+relative_base] != 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2]+relative_base]
        else:
            i += 3

# Vergleich ob der Wert = 0 ist
# Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# Parameter2 gib an ob die Prüfung = 0 lt. Position (0) oder direktem Wert (1) erfolgen soll
# OPCODE 6
def op_false(in1, in2):
    global i
    global relative_base
    if in2 == '0':
        if liste[liste[i+1]] == 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2]+relative_base]
        else:
            i += 3
    elif in2 == '1':
        if liste[i + 1] == 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2] + relative_base]
        else:
            i += 3
    elif in2 == '2':
        if liste[liste[i+1]+relative_base] == 0:
            if in1 == '0':
                i = liste[liste[i + 2]]
            elif in1 == '1':
                i = liste[i + 2]
            elif in1 == '2':
                i = liste[liste[i + 2]+relative_base]
        else:
            i += 3

# 2 Werte werden verglichen - wenn < wird 1 ausgegeben - sonst 0
# # Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# # Parameter2 gib an ob die Prüfung lt. Position (0) oder direktem Wert (1) erfolgen soll
# OPCODE 7:
def op_less(in0, in1, in2):
    global i
    global relative_base
    if in2 == '0':
        v1 = liste[liste[i + 1]]
    elif in2 == '1':
        v1 = liste[i + 1]
    elif in2 == '2':
        v1 = liste[liste[i + 1]+relative_base]

    if in1 == '0':
        v2 = liste[liste[i + 2]]
    elif in1 == '1':
        v2 = liste[i + 2]
    elif in1 == '2':
        v2 = liste[liste[i + 2]+relative_base]

    if v1 < v2:
        if in0 == '0': liste[liste[i + 3]] = 1
        elif in0 == '1': liste[i + 3] = 1
        elif in0 == '2':
            try:
                liste[liste[i + 3] + relative_base] = 1
            except:
                memory_extend(liste[liste[i + 3] + relative_base])
                liste[liste[i + 3] + relative_base] = 1
    elif v1 >= v2:
        if in0 == '0': liste[liste[i + 3]] = 0
        elif in0 == '1': liste[i + 3] = 0
        elif in0 == '2':
            try:
                liste[liste[i + 3] + relative_base] = 0
            except:
                memory_extend(liste[liste[i + 3] + relative_base])
                liste[liste[i + 3] + relative_base] = 0
    i += 4

# 2 Werte werden verglichen - wenn = wird 1 ausgegeben - sonst 0
# # Parameter1 gibt an ob der Pointer lt. Position (0) oder direkter Wert (1) gesetzt werden soll
# # Parameter2 gib an ob die Prüfung lt. Position (0) oder direktem Wert (1) erfolgen soll
# OPCODE 8
def op_equal(in0, in1, in2):    # in2 ist der 1. Parameter nach dem Code, dann in1 und dann in0 wor der Werte gespeichert werden soll
    global i
    global relative_base
    if in2 == '0':
        v1 = liste[liste[i + 1]]
    elif in2 == '1':
        v1 = liste[i + 1]
    elif in2 == '2':
        v1 = liste[liste[i + 1] + relative_base]

    if in1 == '0':
        v2 = liste[liste[i + 2]]
    elif in1 == '1':
        v2 = liste[i + 2]
    elif in1 == '2':
        v2 = liste[liste[i + 2] + relative_base]

    if v1 == v2:
        if in0 == '0': liste[liste[i + 3]] = 1
        elif in0 == '1': liste[i + 3] = 1
        elif in0 == '2':
            try:
                liste[liste[i + 3] + relative_base] = 1
            except:
                memory_extend(liste[liste[i + 3] + relative_base])
                liste[liste[i + 3] + relative_base] = 1
    elif v1 != v2:
        if in0 == '0': liste[liste[i + 3]] = 0
        elif in0 == '1': liste[i + 3] = 0
        elif in0 == '2':
            try:
                liste[liste[i + 3] + relative_base] = 0
            except:
                memory_extend(liste[liste[i + 3] + relative_base])
                liste[liste[i + 3] + relative_base] = 0
    i += 4

# OPCODE 9
def op_relative(in1):
    global i
    global relative_base
    if in1 == '0':
        relative_base += liste[liste[i+1]]
    elif in1 == '1':
        relative_base += liste[i+1]
    elif in1 == '2':
        relative_base += liste[liste[i+1]+relative_base]
    else: print("Error op_relative", in1)
    i += 2

def val_instruct(in1, in2):         # v1 erste Zahl nach operand xx z.B. 01, v2 zweite Zahlen nach 01
    global i
    global relative_base
    if in2 == '0':
        v1 = liste[liste[i + 1]]
    elif in2 == '1':
        v1 = liste[i + 1]
    elif in2 == '2':
        v1 = liste[liste[i + 1]+relative_base]
    else:
        print("ErrorA! ", in2)
    if in1 == '0':
        v2 = liste[liste[i + 2]]
    elif in1 == '1':
        v2 = liste[i + 2]
    elif in1 == '2':
        v2 = liste[liste[i + 2]+relative_base]
    else:
        print("ErrorB! ", in1)
    return v1, v2


# Eigentlichs Herzstück des Int-Computers
# bei optout wird ergebnis der Funktion zurückgegeben
def int_comp(code1,code2):
    global i, inp_inst, loop, mode, relative_base, robo_color, robo_dir
    if liste[i] == 99:
        if mode == 'LOOP':
            loop = False
            return (code2)
        elif mode == 'TEST':
            break
        elif mode == 'ROBOT':
            break
    if liste[i] == 1:
        op_add(liste[i + 3], liste[liste[i + 1]], liste[liste[i + 2]])
        continue
    if liste[i] == 2:
        if liste[i+1] > len(liste): memory_extend(liste[i+1]+5)
        if liste[i+2] > len(liste): memory_extend(liste[i+2]+5)
        if liste[i+3] > len(liste): memory_extend(liste[i+3]+5)
        op_mult(liste[i + 3], liste[liste[i + 1]], liste[liste[i + 2]])
        continue
    if liste[i] == 3:
        if mode == "ROBOT":
            if grid[x][y] == 'B': op_in('I',0)
            elif grid[x][y] == ' ': op_in('I',1)
        else:
            if inp_inst == 0:
                inp_inst += 1
                op_in('I',code1)    # bei der ersten Ansteuerung des Amplifiers wird der Initialwert aus dem 5-stelligen Code genommen
            elif inp_inst == 1:
                op_in('I',code2)    # ab dem 2.Lauf wird immer der aktuelle Out-Wert (=Out-Wert des letzten Amplifier) genommen
            else:
                op_in('0',0)
        continue
    if liste[i] == 4:
        if mode == 'LOOP':
            erg = op_out('0')
            i += 2
            return (erg)
        elif mode == 'TEST':
            op_out('0')
        elif mode == 'ROBOT':
            op_out('0')
        continue
    if liste[i] == 5:
        op_true('0', '0')
        continue
    if liste[i] == 6:
        op_false('0', '0')
        continue
    if liste[i] == 7:
        op_less('0','0','0')
        continue
    if liste[i] == 8:
        op_equal('0','0','0')
        continue
    if liste[i] == 9:
        op_relative('0')
        continue
    if liste[i] > 4:
        instruct = str(liste[i])
        while len(instruct) < 5: instruct = '0' + instruct
        opcode = instruct[3:]

        if opcode == '01':
            memory_check(instruct[0],[liste[i+3]+relative_base])
            value1, value2 = val_instruct(instruct[1], instruct[2])     #v1 erste Zahl nach 01, v2 zweite Zahlen nach 01
            if instruct[0] == '0': op_add(liste[i + 3], value1, value2)
            elif instruct[0] == '1': op_add(i+3, value1, value2)
            elif instruct[0] == '2': op_add(liste[i + 3] + relative_base, value1, value2)
        elif opcode == '02':
            memory_check(instruct[0], [liste[i + 3]+relative_base])
            value1, value2 = val_instruct(instruct[1], instruct[2])     #v1 erste Zahl nach 01, v2 zweite Zahlen nach 01
            if instruct[0] == '0': op_mult(liste[i + 3], value1, value2)
            elif instruct[0] == '1': op_mult(i+3, value1, value2)
            elif instruct[0] == '2': op_mult(liste[i + 3] + relative_base, value1, value2)
        elif opcode == '03':
            if mode == "ROBOT":
                if grid[x][y] == 'B':
                    op_in('I', 0)
                elif grid[x][y] == ' ': op_in('I', 1)
            else:
                op_in(instruct[2],0)
        elif opcode == '04':
            if mode == 'LOOP':
                erg=op_out(instruct[2])
                return (erg)
            elif mode == 'TEST':
                op_out(instruct[2])
            elif mode == 'ROBOT':
                op_out(instruct[2])
        elif opcode == '05':
            op_true(instruct[1],instruct[2])
        elif opcode == '06':
            op_false(instruct[1],instruct[2])
        elif opcode == '07':
            op_less(instruct[0],instruct[1],instruct[2])
        elif opcode == '08':
            memory_check(instruct[2]+instruct[1]+instruct[0], [liste[i + 1], liste[i+2], liste[i+3]])
            op_equal(instruct[0],instruct[1],instruct[2])
        elif opcode == '09':
            memory_check(instruct[2], [liste[i + 1]+relative_base])
            op_relative(instruct[2])
        else: print ("Error OPCODE ", opcode)