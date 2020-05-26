#with open("input06tst.txt") as f:
with open("input06.txt") as f:
    lines = [x.strip() for x in f.readlines()]

erg = ""
for i in range(len(lines[0])):
    chars = {}
    min_key = min_val = 9999999999999
    for j in lines:
        if j[i] in chars: chars[j[i]] += 1
        else: chars[j[i]] = 1
    for key,val in chars.items():
        if val < min_val:
            min_val = val
            min_key = key
    erg = erg + min_key
print(erg)









