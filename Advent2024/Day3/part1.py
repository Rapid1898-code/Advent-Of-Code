import os 
import sys
import re

baseString = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

idxList = [x.start() for x in re.finditer("mul", baseString)]
for checkIDX in idxList:
  workIDX = checkIDX



