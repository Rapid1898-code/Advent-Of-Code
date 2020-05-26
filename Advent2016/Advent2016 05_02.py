#inp = "abc"
inp = "ffykfhsq"

import hashlib

erg = ["" for x in range(8)]
idx=0
while True:
    if idx % 100000 == 0: print(idx)
    hash = hashlib.md5((inp+str(idx)).encode('utf-8')).hexdigest()
    idx += 1
    if hash[0:5] == "00000":

        print(hash)
        print(erg)

        if hash[5].isdigit():
            if int (hash[5]) > 7: continue
        else: continue
        if erg[int(hash[5])] == "": erg[int(hash[5])] = hash[6]
    if "" not in erg: break

str = ""
for i in erg: str = str + i
print(str)








