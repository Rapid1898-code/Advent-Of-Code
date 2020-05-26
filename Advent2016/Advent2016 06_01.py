#with open("input06tst.txt") as f:
with open("input06.txt") as f:
    lines = [x.strip() for x in f.readlines()]

erg = ""
for i in range(len(lines[0])):
    chars = {}
    max_key = max_val = 0
    for j in lines:
        if j[i] in chars: chars[j[i]] += 1
        else: chars[j[i]] = 1
    for key,val in chars.items():
        if val > max_val:
            max_val = val
            max_key = key
    erg = erg + max_key
print(erg)









