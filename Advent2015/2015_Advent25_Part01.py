erg = []

value = 20151125
for i in range(1,6000):
    tempx=0
    tempy=i
    for j in range(1,i):
        tempx += 1
        tempy -= 1
        #erg.append([tempx,tempy,value])
        if tempx == 3029 and tempy == 2947: erg.append ([tempx, tempy, value])
        if tempx % 100 == 0: print(tempx,tempy)
        value = (value*252533) % 33554393
print(erg)

#Enter the code at row 2947, column 3029.


