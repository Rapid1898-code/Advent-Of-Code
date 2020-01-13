import itertools

def SumTheList(thelist, target):
    arr = []
    p = []
    if len(thelist) > 0:
        for r in range(0,12):
            arr += list(itertools.combinations(thelist, r))
        for item in arr:
            if sum(item) == target:
                p.append(item)
    return p

erg = SumTheList([1,3,5,11,13,17,19,23,29,31,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113], 516)
erg.sort(key=len)

# erg = SumTheList([5,11,17,19,23,29,31,41,43,47,53,59,67], 516)
# erg.sort(key=len)

#erg = SumTheList([1,2,3,4,5,7,8,9,10,11], 20)
#erg.sort(key=len)

pos = 0
left = []
end_kombis = []
while pos < len(erg):
    temp_erg = [erg[pos]]
    middle = erg[pos]
    for idx_kombi in range(pos+1,len(erg)):
        find = True
        for element in erg[idx_kombi]:
            if element in middle:
                find = False
                break
            if len(temp_erg) == 2:
                if element in left:
                    find = False
                    break
        if find == True:
            temp_erg.append(erg[idx_kombi])
            if len(temp_erg) == 2: left = list(erg[idx_kombi])
        if len(temp_erg) == 3:
            end_kombis.append(temp_erg)
            length = len (erg[pos])
            break
    print(temp_erg)
    pos += 1

print(temp_erg)
print(end_kombis)

while len(erg[pos]) == len(end_kombis[0][0]):
    middle = erg[pos]
    temp_erg = [erg[pos]]
    for idx_kombi in range(pos+1,len(erg)-1):
        find = True
        for element in erg[idx_kombi]:
            if element in middle: find = False
            if len (temp_erg) == 2:
                if element in left: find = False
        if find == True:
            temp_erg.append (erg[idx_kombi])
            if len (temp_erg) == 2: left = list (erg[idx_kombi])
        if len (temp_erg) == 3:
            end_kombis.append (temp_erg)
            break
    pos += 1

print(end_kombis)

final_erg = []
min_qe = 999999
for idx in end_kombis:
    temp_mlt = 1
    for idx2 in idx[0]: temp_mlt *= idx2
    if temp_mlt < min_qe:
        min_qe = temp_mlt
        final_erg = list(idx)

print (final_erg)
print (min_qe)


















