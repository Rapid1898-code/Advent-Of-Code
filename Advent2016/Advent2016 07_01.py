#lines = ["rxpusykufgqujfe[rypwoorxdemxffui]cvvcufcqmxoxcphp[witynplrfvquduiot]vcysdcsowcxhphp[gctucefriclxaonpwe]jdprpdvpeumrhokrcjt"]
#lines = ["abba[mnop]qrst","abcd[bddb]xyyx","aaaa[qwer]tyui","ioxxoj[asdfgh]zxcvbn"]
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
        i_new = i_new.replace(j,"    ")

    print(klammern)
    print(i_new)

    for j in klammern:
        if check_abba(j):
            check = False
            break
    if check == False: continue
    if check_abba(i_new):
        print(i)
        sum += 1

print(sum)












