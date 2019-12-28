with open('Advent08.txt') as f:
    lines = [x.strip() for x in f.readlines()]
count_overall = count_memory = 0

#lines = ['""','"abc"','"aaa\\"aaa"','"\\x27"']

for line in lines:
    idx = 0
    leng = len(line)
    single_overall = 2
    count_overall += 2      # Anführungszeichen am Anfang und Ende
    while idx < leng:
        check_char = line[idx]
        if line[idx] == '"':
            count_overall += 2
            single_overall += 2
            idx += 1
        elif line[idx] == '\\':
            count_overall += 2
            single_overall += 2
            idx += 1
        else:
            idx += 1
            count_overall += 1
            single_overall +=1
    print (single_overall, line)

print(count_overall)
print(count_overall - 6310)     # minus result from Part1











