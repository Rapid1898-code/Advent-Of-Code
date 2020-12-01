def adv1 (listInp):
    for idx,elem in enumerate(listInp):
        for idx2 in range(idx+1,len(listInp)-1,1):
            erg = int(elem) + int(listInp[idx2])
            if erg == 2020:
                return(int(elem) * int(listInp[idx2]))

with open("advent01.txt","r") as f:
    listInp = [x.strip() for x in f.readlines()]

print(adv1(listInp))
