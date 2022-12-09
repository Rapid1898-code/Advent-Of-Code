# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')

with open("inp.txt","r") as f:
  inp = [x.strip() for x in f.readlines()]

def changePos(head, tail, wDir, wLen, posFinds):
  posH_X, posH_Y = head
  posT_X, posT_Y = tail
  for i in range(wLen):
    # change head position
    if wDir == "L":
      posH_X -= 1
    elif wDir == "R":
      posH_X += 1
    elif wDir == "U":
      posH_Y += 1
    elif wDir == "D":
      posH_Y -= 1

    # adapt tail position
    if posH_X - posT_X > 1:
      if posH_X < 0:
        posT_X = posH_X + 1
      elif posH_X > 0:
        posT_X = posH_X - 1
      elif posH_X == 0:
        if posT_X < 0:
          posT_X = -1
        else:
          posT_X = 1
    
    if posH_Y - posT_Y > 1:
      if posH_Y > 0:
        posT_Y += 1
        if posH_X > posT_X:
          posT_X += 1
        if posH_X < posT_X:
          posT_X -= 1
      elif posH_Y < 0:
        posT_Y -= 1
        if posH_X > posT_X:
          posT_X += 1
        if posH_X < posT_X:
          posT_X -= 1
      elif posH_Y == 0:
        if posT_Y < 0:
          posT_Y = -1
          posT_X = 0
        else:
          posT_Y = 1
          posT_X = 0    
         
    if [posT_X, posT_Y] not in posFinds:
      posFinds.append([posT_X, posT_Y])

  return([posH_X, posH_Y], [posT_X, posT_Y], posFinds)


posFinds = []
posHead = [0,0]
posTail = [0,0]
for e in inp:
  wDir = e.split()[0]
  wLen = int(e.split()[1])
  print (posHead, posTail, e)
  posHead, posTail, posFinds = changePos(posHead, posTail, wDir, wLen, posFinds)
  print (posHead, posTail)
  print (posFinds)
  input("Press!")

  



