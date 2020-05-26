#lines = ["aaaaa-bbb-z-y-x-123[abxyz]","a-b-c-d-e-f-g-h-987[abcde","not-a-real-room-404[oarel]","totally-real-room-200[decoy]"]
with open ("input04.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sum = 0
for i in lines:
    idx = 0
    chars = {}
    while True:
        if i[idx].isdigit(): break
        if i[idx] in chars: chars[i[idx]] += 1
        elif i[idx] != "-": chars[i[idx]] = 1
        idx += 1
    code = ""
    while True:
        if i[idx] == "[": break
        else: code += i[idx]
        idx += 1
    checksum = i[idx+1:idx+6]

    idx2 = 0
    check = True
    chars = {k: v for k, v in sorted(chars.items(), key=lambda x: (-x[1],x[0]))}

    print(chars)

    for key in chars.keys():
        if idx2 == 5: break

        #print(chars[key])
        #print(checksum[idx2])

        if key != checksum[idx2]:
            check = False
            break
        idx2 += 1



    if check == True: sum += int(code)
print(sum)






