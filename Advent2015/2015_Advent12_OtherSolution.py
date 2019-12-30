import json
import re


with open('Advent12.txt') as f:
    s = f.read()

# Part one
print(sum(map(int, re.findall(r'-?\d+', s))))


# Part two
def get_sum(d):
    if isinstance(d, int):
        return d
    elif isinstance(d, str):
        return 0
    elif isinstance(d, list):
        return sum(get_sum(x) for x in d)
    else:
        return 0 if any(x == 'red' for x in d.values()) else sum(get_sum(x) for x in d.values())


d = json.loads(s)

print(d.values())
for x in d:
    print(x)

print(get_sum(d))