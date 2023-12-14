import os 
import sys
import string

if __name__ == '__main__':
  path = os.path.abspath(os.path.dirname(sys.argv[0])) 
  fn = os.path.join(path, "inp.txt")
  with open(fn, encoding="utf8", errors="ignore") as f:
    lines = f.read().splitlines()

  inpDict = {}
  for l in lines:
    wGameNr = int(l.split()[1].replace(":",""))
    worker = l.split()[2:]

    dictVal = {}
    for i,e in enumerate(worker):
      if i % 2 == 0:
        checkVal = worker[i+1].replace(",","").replace(";","")
        if checkVal not in dictVal:
          dictVal[checkVal] = int(e)
        else:
          dictVal[checkVal] += int(e)         
        # print(dictVal)
        # input("Press!")
    inpDict[wGameNr] = dictVal

  countSummary = 0
  for k, v in inpDict.items():
    if v["red"] <= 12 \
      and v["green"] <= 13 \
      and v["blue"] <= 14:
        countSummary += k
    # print(k, v)
    # print(countSummary)
    # input("Press!")



  print(countSummary)
