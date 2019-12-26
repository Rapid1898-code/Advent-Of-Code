tot = 0
liste=[]
vowels = "aeiou"
bads = ["ab", "cd", "pq", "xy"]
part1 = part2 = 0

file = open("Advent05.txt", "r")    # Input-Elemente aus Datei in Liste lesen
for line in file:
    liste.append(line.rstrip())
file.close()

for line in liste:
    # part 1
    v_cnt = 0
    double = bad = False
    for v in vowels:
      v_cnt += line.count(v)
    for i in range (0, len(line) - 1):
      if line[i] == line[i+1]:
        double = True
    for b in bads:
      if line.find(b) > -1:
        bad = True
    if v_cnt > 2 and double and not bad:
      part1 += 1

    # part 2
    pairs = repeats = False
    for i in range (0,len(line)-2):
      a,b,c = line[i:i+3]
      if a == c:
        repeats = True
      if line.count(a+b) > 1:
        pairs = True
    if repeats and pairs:
      print(line)
      part2 += 1


print(part2)