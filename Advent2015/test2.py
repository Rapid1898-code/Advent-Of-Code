import re
m=[]
[m.start() for m in re.finditer('test', 'test test test test')]
print(m)