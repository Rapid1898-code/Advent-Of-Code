with open('Advent08.txt') as f:
    lines = [x.strip() for x in f.readlines()]
count_overall = count_memory = 0

print(lines)
#lines = ['"sjdivfriyaaqa\\xd2v\\"k\\"mpcu\\"yyu\\"en"']
#lines = ['""','"abc"','"aaa\\"aaa"','"\\x27"']
#lines = ['"aaa\\"aaa"']
#lines = ['"\\x27"']
#lines = ['"yrbajyndte\\rm"']

for line in lines:
    idx = 0
    leng = len(line)
    single_overall = 0
    single_memory = 0
    while idx < leng:
        check_char = line[idx]
        if line[idx] == '"' and (idx == 0 or idx == len(line)-1):
            idx += 1
            count_overall += 1
            single_overall += 1
            continue
        elif line[idx] == '\\' and line[idx+1] == 'x':
            idx += 4
            count_memory += 1
            single_memory += 1
            count_overall += 4
            single_overall += 4
        elif line[idx] == '\\' and line[idx+1] == '"':
            idx += 2
            count_memory += 1
            single_memory += 1
            count_overall += 2
            single_overall += 2
        elif line[idx] == '\\' and line[idx+1] != 'x' and line[idx+1] != '"':
            idx += 2
            count_memory += 1
            single_memory += 1
            count_overall += 2
            single_overall += 2
        else:
            idx += 1
            count_memory += 1
            single_memory += 1
            count_overall += 1
            single_overall += 1
    print (single_overall, single_memory, single_overall-single_memory, line)

print(count_overall)
print(count_memory)
print(count_overall-count_memory)










