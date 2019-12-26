import hashlib
count = 0
input= "ckczppom"
#input = "abcdef"

while True:
    check_ungleich_zero = False
    count += 1
    temp_try = input + str(count)
    result = hashlib.md5(temp_try.encode())
    result_hex = result.hexdigest()

    for i in range(5):
        # print(result_hex[i])
        # print(result_hex[i]!="0")
        if result_hex[i] != "0": check_ungleich_zero = True
    if check_ungleich_zero == False: break

    # if count == 609043: break
    # print (temp_try,result_hex)

print(count)