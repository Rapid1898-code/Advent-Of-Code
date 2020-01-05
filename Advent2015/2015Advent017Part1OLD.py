with open('2015Advent017Input1.txt') as f:
    liste = [int(x.strip()) for x in f.readlines()]
target=25
solutions_count = 0
solutions_list = []
liste=[20,15,10,5,5]

for idx in range[len(liste)-1]:
    temp_check = liste[idx]
    temp_check_list = []
    temp_check_list.append(liste[idx])
    idx2 = idx +1
    while idx2 < len(liste):
        if liste[idx] + liste[idx2] == target:
            temp_check_list.append(liste[idx2])
            solutions_list.apppend(temp_check_list)
            solutions_count += 1
        if liste[idx] + liste[idx2] > target:
            idx2 += 1
        if liste[idx] + liste[idx2] < target:
            temp_check_list.append(liste[idx2])
            idx2 +=1


