#lines = ["qzmt-zixmtkozy-ivhz-343[abxyz]"]
with open ("input04.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sum = 0
for i in lines:
    idx = 0
    while True:
        if i[idx].isdigit(): break
        idx += 1
    name = i[0:idx-1]

    idx_start_id = idx
    while True:
        if i[idx] == "[": break
        idx += 1
    id = int(i[idx_start_id:idx])

    for j in range(id):
        for idx,char in enumerate(name):
            if char == " ": continue
            elif char == "-": name = name[:idx] + " " + name[idx + 1:]
            elif ord (char) == 122: name = name[:idx] + "a" + name[idx + 1:]
            else: name = name[:idx] + chr (ord (char) + 1) + name[idx + 1:]

    if "north" in name: print (id,name)




