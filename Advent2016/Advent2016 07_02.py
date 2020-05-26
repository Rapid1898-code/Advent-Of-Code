#lines = ["rxpusykufgqujfe[rypwoorxdemxffui]cvvcufcqmxoxcphp[witynplrfvquduiot]vcysdcsowcxhphp[gctucefriclxaonpwe]jdprpdvpeumrhokrcjt"]
#lines = ["aba[bab]xyz","xyx[xyx]xyx","aaa[kek]eke","aaa[kek]eke"]
with open("input07.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sum = 0
def check_abba(s):
    for i in range(len(s)-3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]: return True
    return False

for i in lines:
    klammern = []
    to_del = []
    check = True
    for j in range(len(i)-1,0,-1):
        if i[j] not in ["[","]"]: continue
        elif i[j] == "]": end = j+1
        elif i[j] == "[":
            klammern.append(i[j:end])
    i_new = i
    for j in klammern:
        i_new = i_new.replace(j," ")
    i_list = i_new.split()

    kombi_innen = []
    kombi_aussen = []

    for j in klammern:
        for k in range(len(j)-2):
            if j[k] == j[k+2]: kombi_innen.append(j[k:k+3])
    for j in i_list:
        for k in range(len(j)-2):
            if j[k] == j[k+2]: kombi_aussen.append(j[k:k+3])

    for j in kombi_innen:
        check = j[1]+j[0]+j[1]
        if check in kombi_aussen:
            print(j,check,i)
            sum += 1
print(sum)












