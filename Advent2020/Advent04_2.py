import re

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
    tmpValues = []
    tmpKeys = []
    for entry in block:
        for i in entry.split(" "):
            tmpKeys.append(i.split(":")[0])
            tmpValues.append(i.split(":")[1])
    keys.append(tmpKeys)
    pairs.append(dict(zip(tmpKeys, tmpValues)))
# print(keys)
# for i in pairs: print(i)

countPassports = 0
for passport in pairs:
    if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
        check = True
        if int(passport["byr"]) < 1920 or int(passport["byr"]) > 2002:
            check = False
            # print(f"Invalid birth {passport['byr']}")
        if not passport["byr"].isdigit () or len (passport["byr"]) != 4:
            check = False
            # print(f"Invalid birth {passport['byr']}")
        if int(passport["iyr"]) < 2010 or int(passport["iyr"]) > 2020:
            check = False
        if not passport["iyr"].isdigit () or len (passport["iyr"]) != 4:
            check = False
            # print(f"Invalid birth {passport['byr']}")
        if int (passport["eyr"]) < 2020 or int (passport["eyr"]) > 2030:
            check = False
        if not passport["eyr"].isdigit () or len (passport["eyr"]) != 4:
            check = False
            # print(f"Invalid birth {passport['eyr']}")
        if "cm" in passport["hgt"]:
            value = passport["hgt"].replace("cm","")
            if int(value) < 150 or int(value) > 193:
                check = False
                # print (f"Invalid birth {passport['hgt']}")
        if "in" in passport["hgt"]:
            value = passport["hgt"].replace("in", "")
            if int (value) < 59 or int (value) > 76:
                check = False
                # print (f"Invalid birth {passport['hgt']}")
        if "cm" not in passport["hgt"] and "in" not in passport["hgt"]:
            check = False
            print (f"CM and IN not: {passport['hgt']}")
        pattern1 = re.compile ("^#[0-9a-f]{6}$")
        if pattern1.match(passport["hcl"]) == None:
            check = False
            # print (f"Invalid birth {passport['hcl']}")
        if passport["ecl"] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
            check = False
            # print (f"Invalid birth {passport['ecl']}")
        if not passport["pid"].isdigit() or len(passport["pid"]) != 9:
            check = False
            # print (f"Invalid birth {passport['pid']}")
        if check:
            countPassports += 1
            # print(passport)

print(f"Number of valid passports: {countPassports}")








