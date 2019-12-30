pw = 'hxbxxzaa'
#pw = 'hijklmmn'
#pw = 'abbceffg'
#pw = 'abbcegjk'
#pw = 'abcdffaa'
#pw = 'ghjaabcc'
#pw = 'hxbxxxyz'

def check_pw(string):
    increasing_three = two_diff_pairs = False
    temp_two_diff_pairs = ''
    temp_two_diff_pairs_pos = 0
    for idx in range(6):
        if ord(string[idx]) == ord(string[idx+1])-1 == ord(string[idx+2])-2:
            increasing_three = True
    for idx in range(len(string)-1):
        if string[idx] in ['i','o','l']: return False
        if idx < len(string)-1 and string[idx] == string[idx+1] and idx != temp_two_diff_pairs_pos:
            if temp_two_diff_pairs == '':
                temp_two_diff_pairs = string[idx]+string[idx+1]
                temp_two_diff_pairs_pos = idx+1
            else:
                two_diff_pairs = True
    if increasing_three and two_diff_pairs: return True
    else: return False

print(check_pw(pw))

pw = pw.replace('i','j')
pw = pw.replace('o','p')
pw = pw.replace('l','m')

while not check_pw(pw):
    print(pw)
    idx = -1
    temp_string = temp_char = ''
    if pw[idx] == 'z':
        while pw[idx] == 'z':
            temp_char = 'a' + temp_char
            idx -= 1
        temp_char = chr(ord(pw[idx])+1) + temp_char
        pw = pw[:8-len(temp_char)] + temp_char
    else:
        temp_char = chr(ord(pw[idx])+1)
        pw = pw[:7] + str(temp_char)

print(pw)




