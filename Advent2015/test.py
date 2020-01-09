import itertools
# weapons = {'W1':(8,4,0), 'W2':(10,5,0), 'W3':(25,6,0), 'W4':(40,7,0),'W5':(74,8,0)}
# for w in weapons:
#     print(weapons.get(w))

ring_kombis = [0,1,2,3,4,5,6]
kombi = itertools.combinations([1,2,3,4,5,6],2)
for i in kombi: ring_kombis.append(i)
print (ring_kombis)















