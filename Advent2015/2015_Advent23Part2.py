input=[]
with open('Advent23.txt') as f:
    src = [x.strip().split() for x in f.readlines()]
for i in src:
    if len(i)==2:
        if i[1] in ['a','b']: input.append((i[0],i[1]))
        else: input.append((i[0],int(i[1])))
    else: input.append((i[0],i[1][0],int(i[2])))

print (input)
#input = [('inc', 'a'), ('jio', 'a', 2), ('tpl', 'a'), ('inc', 'a')]

pos = 0
value = [1,0]

while True:
    if input[pos][1] == 'a': temp_idx = 0
    else: temp_idx = 1
    if input[pos][0] == 'hlf':
        value[temp_idx] /= 2
        pos +=1
    elif input[pos][0] == 'tpl':
        value[temp_idx] *= 3
        pos +=1
    elif input[pos][0] == 'inc':
        value[temp_idx] += 1
        pos +=1
    elif input[pos][0] == 'jmp':
        pos += input[pos][1]
    elif input[pos][0] == 'jie':
        if value[temp_idx] % 2 == 0: pos += input[pos][2]
        else: pos += 1;
    elif input[pos][0] == 'jio':
        if value[temp_idx] == 1: pos += input[pos][2]
        else: pos += 1;
    if pos >= len(input) or pos < 0: break
    print (value)

print('A= ',value[0])
print('B= ',value[1])