#with open("input12TST.txt") as f:
with open("input12.txt") as f:
    lines = [x.strip() for x in f.readlines()]
for idx,cont in enumerate(lines):
    lines[idx] = cont.split()

idx = 0
reg = {"a":0, "b":0, "c":0, "d":0, "1":0}
while idx < len(lines):
    if lines[idx][0] == "cpy":
        if lines[idx][1] in ["a","b","c","d"]: reg[lines[idx][2]] = reg[lines[idx][1]]
        else: reg[lines[idx][2]] = int(lines[idx][1])
        idx += 1
    elif lines[idx][0] == "inc":
        reg[lines[idx][1]] += 1
        idx += 1
    elif lines[idx][0] == "dec":
        reg[lines[idx][1]] -= 1
        idx += 1
    elif lines[idx][0] == "jnz":
        if reg[lines[idx][1]] == 0:
            idx += 1



        else: idx = idx + int(lines[idx][2])

    #print(reg)

print(reg["a"])
