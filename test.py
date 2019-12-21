import itertools

combi =[]
liste = [1,2,3,4,5,10]

def make_combi():
  perm = itertools.product(liste, repeat=2)
  for i in perm:
    if i[0] == i[1] and i[0] != "1": continue
    if i[0] == "0" and i[1] != "1": continue
    if i[1] == "0" and i[0] != "1": continue
    combi.append([int(i[0]), int(i[1])])
  combi.sort()

make_combi()
print (combi)















