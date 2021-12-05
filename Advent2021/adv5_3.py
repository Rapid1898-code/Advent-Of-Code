from collections import Counter
import re

with open("adv5.txt") as f:
    inp = f.readlines()

nums = [[int(n) for n in re.findall("\d+", line)] for line in inp]

hv = []
diag = []
for x1, y1, x2, y2 in nums:
    hvpts = []
    dpts = []
    if x1 == x2:
        hvpts = [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        hvpts = [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    elif abs(x1 - x2) == abs(y1 - y2):
        x_step, x_offset = (1, 1) if x1 < x2 else (-1, -1)
        y_step, y_offset = (1, 1) if y1 < y2 else (-1, -1)
        xs = list(range(x1, x2 + x_offset, x_step))
        ys = list(range(y1, y2 + y_offset, y_step))
        dpts = list(zip(xs, ys))
    
    hv.extend(hvpts)
    diag.extend(dpts)

cnt_hv = Counter(hv)
print(sum([1 for v in cnt_hv.values() if v > 1]))
cnt_all = Counter(hv+diag)
print(sum([1 for v in cnt_all.values() if v > 1]))
