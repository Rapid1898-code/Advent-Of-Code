import math
liste=[]
source=[]

def format_input():
    file = open("Advent14temp5.txt", "r")
    for line in file:
        liste.append(line.rstrip())
    file.close()
def interpret_input(temp_string):
    for i in range(0,len(temp_string)):
        zahl=''
        temp_num = 0
        if i >= len(temp_string): break
        if temp_string[i].isdigit() == True:
            for k in range(i+1, len(temp_string)):
                if temp_string[k].isdigit() == False:
                    temp_num = temp_string[:k]
                    temp_string = temp_string[k + 1:]
                    for j in range(0, len(temp_string)):
                        if temp_string[j] == ',':
                            temp_string = temp_string[:j]
                            temp_string = temp_string.strip()
                    temp_num = temp_num.replace(',','')
                    temp_num = temp_num.strip()
                    temp_num = int(temp_num)
                    return(temp_num, temp_string)
def read_source():
    for i in liste:
        for j in range(0, len(i)):
            if i[j] == '=' and i[j + 1] == '>':
                part1 = i[:j] + ','
                part2 = i[j + 2:] + ','
                inhalt = []
                start = 0
                for k in range(0, len(part1)):
                    if part1[k] == ',':
                        temp_part1 = part1[start:k + 1]
                        numb, text = interpret_input(temp_part1)
                        start = k
                        inhalt.append(numb)
                        inhalt.append(text)
                numb2, text2 = interpret_input(part2)
        # source.append(inhalt)
        # source.append(numb2)
        # source.append(text2)
        source.append([inhalt, numb2, text2])

def find_element(liste, search):
    for i in range(0, len(liste)):
        if liste[i][2] == search: return(i)
    return(None)

def find_result(liste,search):
    for i in range(0, len(liste)):
        if result[i][0] == search: return(i)
    return(None)

def find_rest(liste,search):
    for i in range(0, len(liste)):
        if rest[i][0] == search: return(i)
    return(None)

def find_workinglist(liste,search):
    for k in range(0, len(liste)):
        if new_working_list[k] == search: return k
    return(None)

def result_update(name, number):
    idx = find_result(result,name)
    if idx == None:
        result.append([name, number])
    else:
        result[idx][1] += number

result = []       # needes amount, name
rest = []
ore = []
format_input()
read_source()

print(source)
idx = find_element(source,'FUEL')
working_list = list(source[idx][0])
while True:
    new_working_list = []
    # print('One Full replacement: ', working_list)
    # print('Result', result)
    # print('Ore: ',ore)
    if working_list == []: break
    for i in range (0, len(working_list)):
        # print('Intermediate Working List each replacement:', new_working_list)
        if type(working_list[i]) != int and type(working_list[i]) != float:
            idx_work = find_element(source,working_list[i])
            if source[idx_work][0][1] == 'ORE':
                result_update(working_list[i], working_list[i-1])
                if source[idx_work] not in ore: ore.append(source[idx_work])
            else:
                for j in range(0,len(source[idx_work][0])):     # looping the elements on higher level
                    if type(source[idx_work][0][j]) == int or type(source[idx_work][0][j]) == float:
                        idx_rest2 = find_rest(rest,source[idx_work][0][j+1])
                        if idx_rest2 == None:
                            rest_diff = 0
                        else: rest_diff = rest[idx_rest2][1]
                        idx_rest = find_rest(rest, working_list[i])
                        if idx_rest == None: rest_diff = 0
                        else: rest_diff = rest[idx_rest][1]

                        if working_list[i-1]-rest_diff < source[idx_work][1]:
                            temp_num = source[idx_work][0][j]
                        else:
                            temp_num = source[idx_work][0][j] * math.ceil((working_list[i - 1]-rest_diff) / source[idx_work][1])
                        if rest_diff != 0: del rest[idx_rest]
                        if len(new_working_list) == 0:
                            new_working_list.append(temp_num)
                        else:
                            idxwork2 = find_workinglist(new_working_list, source[idx_work][0][j+1])
                            if idxwork2 == None:
                                new_working_list.append(temp_num)
                            else:
                                new_working_list[idxwork2-1] += temp_num
                    else:
                        if source[idx_work][0][j] not in new_working_list:
                            new_working_list.append(source[idx_work][0][j])
                temp_calc = math.ceil(working_list[i - 1] / source[idx_work][1])
                temp_rest = temp_calc * source[idx_work][1] - working_list[i - 1]
                idx_rest = find_rest(rest, working_list[i])
                if temp_rest != 0:
                    if idx_rest == None:
                        rest.append([working_list[i], temp_rest])
                    else:
                        rest[idx_rest][1] += temp_rest
    print('One Full replacement: ', new_working_list)
    print('Result', result)
    print('Ore: ',ore)
    print('Rest: ',rest,'\n')
    working_list = list(new_working_list)

result_end = 0
# print ('Result: ',result)
# print ('Ore: ', ore)

for i in result:
    idx = find_element(ore, i[0])
    tmp_calc = i[1] / ore[idx][1]
    tmp_calc2 = math.ceil(tmp_calc)
    calc = tmp_calc2 * ore[idx][0][0]
    # print(i, calc)
    result_end += calc

print (result_end)