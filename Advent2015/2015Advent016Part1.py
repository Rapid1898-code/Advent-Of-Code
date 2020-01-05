source=[]
target=['children',3,'cats',7,'samoyeds',2,'pomerians',3,'akitas',0,'vizslas',0,'goldfish',5,'trees',3,'cars',2,'perfumes',1]

with open('2015Advent016Input.txt') as f:
    liste = [x.strip() for x in f.readlines()]
for i in liste:
    ts = i.split()
    temp_list = []
    for idx,entry in enumerate(ts):
        if idx==0: temp_list.append(entry)
        elif idx==len(ts)-1: temp_list.append(int(entry))
        else:
            if idx % 2 == 0: temp_list.append(entry[:-1])
            elif idx % 2 == 1: temp_list.append(int(entry[:-1]))
    source.append(temp_list)

def check_sue(c_sue):
    # if c_sue[1]==465:
    #     print('check')
    for idx, entry in enumerate(c_sue):
        if idx == 0 or idx == 1: continue
        if idx % 2 == 0:
            check_name = c_sue[idx]
            check_anz = c_sue[idx + 1]
            for idx2, entry2 in enumerate(target):
                check = False
                if idx2 % 2 == 0:
                    if check_name == target[idx2] and check_anz == target[idx2 + 1]:
                        check = True
                        break
            if check == False:
                # print(c_sue[1],check_name,check_anz,target)
                return False
    return True

for sue in source:
    if check_sue(sue) == True: print(sue)



