liste = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,9,90,224,1001,224,-99,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,1102,26,62,225,1101,11,75,225,1101,90,43,225,2,70,35,224,101,-1716,224,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1101,94,66,225,1102,65,89,225,101,53,144,224,101,-134,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1102,16,32,224,101,-512,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1001,43,57,224,101,-147,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,36,81,225,1002,39,9,224,1001,224,-99,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1,213,218,224,1001,224,-98,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,102,21,74,224,101,-1869,224,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1101,25,15,225,1101,64,73,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,1002,223,2,223,1005,224,329,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,108,226,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,434,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,479,1001,223,1,223,8,677,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,524,101,1,223,223,1008,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,1107,677,677,224,1002,223,2,223,1006,224,569,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,584,101,1,223,223,1108,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,629,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,644,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,659,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226]  # Liste für Elemente initialisieren
#liste = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
#liste = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
#liste = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
#liste = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

def op_add():
    global i
    print(liste[i:i + 4])
    liste[liste[i + 3]] = liste[liste[i + 1]] + liste[liste[i + 2]]
    i += 4

def op_mult():
    global i
    print(liste[i:i + 4])
    liste[liste[i + 3]] = liste[liste[i + 1]] * liste[liste[i + 2]]
    i += 4

def op_in(inst):
    global i
    print(liste[i:i + 2])
    inp = input("Input: ")
    if inst == '0': liste[liste[i + 1]] = int(inp)
    elif inst == '1': liste[i + 1] = int(inp)
    else: print('Error F! ', inst)
    i += 2

def op_out(inst):
    global i
    print(liste[i:i + 2])
    if inst == '0': print("Output: ", liste[liste[i + 1]])
    elif inst == '1': print("Output: ", liste[i + 1])
    else: print ('Error D! ', inst)
    i += 2

def op_true(in1, in2):
    global i
    print(liste[i:i + 3])
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

def op_false(in1, in2):
    global i
    print(liste[i:i + 3])
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

def op_less(in1, in2):
    global i
    print(liste[i:i + 4])
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

def op_equal(in1, in2):
    global i
    print(liste[i:i + 4])
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

i=0
while True:
    if liste[i] == 99: break
    if liste[i] == 1:
        op_add()
        continue
    if liste[i] == 2:
        op_mult()
        continue
    if liste[i] == 3:
        op_in('0')
        continue
    if liste[i] == 4:
        op_out('0')
        continue
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
        print(liste[i:i + 4])
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
            op_out(instruct[2])
        elif opcode == '05':
            op_true(instruct[1],instruct[2])
        elif opcode == '06':
            op_false(instruct[1],instruct[2])
        elif opcode == '07':
            op_less(instruct[1],instruct[2])
        elif opcode == '08':
            op_equal(instruct[1],instruct[2])
        else: print ("Error E ", opcode)






