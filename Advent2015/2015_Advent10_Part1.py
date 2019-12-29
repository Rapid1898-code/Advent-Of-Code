input = '1113122113'

for i in range(50):
    idx=0
    temp_erg = ''
    while idx < len(input):
        if idx == len(input)-1 or input[idx] != input[idx+1]:
            temp_erg = temp_erg + '1' + input[idx]
            idx +=1
        elif input[idx] == input[idx+1]:
            temp_count = 1
            while idx != len(input)-1 and input[idx] == input[idx+1]:
                temp_count += 1
                idx += 1
            temp_erg = temp_erg + str(temp_count) + input[idx-temp_count+1]
            idx += 1
    input = temp_erg
    print(i, len(input))
print(len(input))


