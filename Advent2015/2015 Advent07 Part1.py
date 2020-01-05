with open('2015Advent07Input.txt') as f:
    liste = [x.strip() for x in f.readlines()]

index = {l.split()[-1]: l for l in liste}

for line in liste:
    print(line)










