# mylist = [1,2,3]
# for i in mylist: print(i)
#
# mylist = [x*x for x in range(5)]
# print(mylist)
#
# mylist = [x-1 for x in range(0,6,2)]
# print(mylist)

# mygenerator =(x*x for x in range(1,5))
# print(mygenerator)
# for i in mygenerator: print(i)

def createGenerator(n):
    mylist = range(n)
    for i in mylist:
        yield i*i

mygenrator = createGenerator(3)
for i in mygenrator: print(i)













