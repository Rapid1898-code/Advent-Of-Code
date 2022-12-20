# import stackprinter
# stackprinter.set_excepthook(style='darkbg2')
import os
import sys

path = os.path.abspath(os.path.dirname(sys.argv[0])) 
fn = os.path.join(path, "inp.txt")
with open(fn,"r") as f:
  inp = [x.strip() for x in f.readlines()]
startP = endP = False
for y,row in enumerate(inp):
  for x,e in enumerate(row):
    if e == "S":
      startP = [y,x]
    if e == "E":
      endP = [y,x]
maxY = len(inp)
maxX = len(inp[0])
workPaths = [[startP]]

def checkPaths(point,matrix):
  res = []
  end = []
  Y = point[0]
  X = point[1]
  v = matrix[Y][X]

  if X + 1 < maxX and \
    (ord(matrix[Y][X+1]) <= ord(v) + 1 or v == "S"):
    if matrix[Y][X+1] != "E":
      res.append([Y, X+1])
    else:
      end.append([Y, X+1])

  if X > 0 and \
    (ord(matrix[Y][X-1]) <= ord(v) + 1 or v == "S"):
    if matrix[Y][X-1] != "E":
      res.append([Y, X-1])
    else:
      end.append([Y, X-1])      

  if Y + 1 < maxY and \
    (ord(matrix[Y+1][X]) <= ord(v) + 1 or v == "S"):
    if matrix[Y+1][X] != "E":
      res.append([Y+1,X])  
    else:
      end.append([Y+1, X])      

  if Y > 0 and \
    (ord(matrix[Y-1][X]) <= ord(v) + 1 or v == "S"):
    if matrix[Y-1][X] != "E":
      res.append([Y-1,X])  
    else:
      end.append([Y-1, X])         
  
  return(res, end)

endList = []
while True:
  print(workPaths)
  input("Press!")
  workPathsNew = []
  for i,p in enumerate(workPaths):
    res,end = checkPaths(p[0],inp)
    for r in res:
      worker = p[:]    
      worker.insert(0,r)   
      workPathsNew.append(worker)
    for e in end:
      endList.append(e)
  workPaths = workPathsNew[:]


