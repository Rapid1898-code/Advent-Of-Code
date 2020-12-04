def readInput(fn,makeInt=False):
    with open (fn, "r") as f:
        listInp = [x.strip () for x in f.readlines ()]
    if makeInt: listInp = [int (x) for x in listInp]
    return(listInp)

inpList = readInput("Advent04.txt")

finalInpList = []
idx = 0
tmpEntry = []
while idx < len(inpList):
    if inpList[idx] != "":
        tmpEntry.append(inpList[idx])
    else:
        finalInpList.append(tmpEntry)
        tmpEntry = []
    if idx + 1 == len(inpList):
        finalInpList.append(tmpEntry)
    idx += 1

pairs = []
keys = []
for block in finalInpList:
    tmpPairs = []
    tmpKeys = []
    for entry in block:
        for i in entry.split(" "):
            tmpKeys.append(i.split(":")[0])
            tmpPairs.append(i)
    keys.append(tmpKeys)
    pairs.append(tmpPairs)
print(keys)
print(pairs)

countPassports = 0
for passport in keys:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        countPassports += 1

print(f"Number of valid passports: {countPassports}")








