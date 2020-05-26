# inp = "abc"
inp = "ffykfhsq"

import hashlib

erg = ""
idx=0
while True:
    if idx % 100000 == 0: print(idx)
    hash = hashlib.md5((inp+str(idx)).encode('utf-8')).hexdigest()
    if hash[0:5] == "00000":
        erg = erg + hash[5]
        print(erg)
    if len(erg) == 8: break
    idx += 1

print(erg)








