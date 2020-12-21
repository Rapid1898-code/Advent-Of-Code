def readInput(fn,mode=0):
    """
    :param fn: input filname
    :param mode:    0 normal working => split at blank
                    1 normal int => split at blank and change to int
                    2 many lines => seperated input with empty lines,
                    3 one line / 2 values => split in char and int
    :return: list with inputs per line
    """
    with open (fn, "r") as f:
        if mode in [0,1]:
            listInp = [x.strip () for x in f.readlines ()]
        elif mode == 2:
            listInp = []
            tmpListInp = []
            for x in f.readlines():
                if x.strip() == "":
                    listInp.append(tmpListInp)
                    tmpListInp = []
                else:
                    tmpListInp.append(x.strip())
            # add last line
            listInp.append (tmpListInp)
        elif mode == 3:
            listInp = [(x.split()[0].strip(),int(x.split()[1].strip())) for x in f.readlines ()]
    if mode == 1:
        listInp = [int (x) for x in listInp]
    return(listInp)

inpTmp = readInput("Advent21.txt",mode=0)
print(inpTmp)

ingredientsDict = {}
ingredientsList = []
allergensDict = {}
allergensList = []
for idx, line in enumerate(inpTmp):
    ingredients = line.split(" (contains")[0].split(" ")
    ingredients.sort()
    allergens = line.split(" (contains ")[1].replace(")","").split(", ")
    allergens.sort()
    ingredientsDict[idx] = ingredients
    allergensDict[idx] = allergens
for key, value in allergensDict.items():
    print(key,value,ingredientsDict[key])
    for elem in value:
        if elem not in allergensList:
            allergensList.append(elem)
    for elem in ingredientsDict[key]:
        if elem not in ingredientsList:
            ingredientsList.append(elem)
allergensList.sort()
ingredientsList.sort()
print(f"AllergensList: {allergensList}")
print(f"IngredientsList: {ingredientsList}")

ergResultList = []
while True:
    findSomething = False
    for elemAllergen in allergensList:
        # find alle existing food with elem
        tmpDict = {}
        tmpIncredients = []
        for idx in range(len(allergensDict)):
            if elemAllergen in allergensDict[idx]:
                tmpDict[idx] = ingredientsDict[idx]
                for elem in ingredientsDict[idx]:
                    if elem not in tmpIncredients:
                        tmpIncredients.append(elem)
                tmpIncredients.sort()
        print(f"\nAllergen: {elemAllergen}")
        for key,val in tmpDict.items():
            print(key,val)
        print(f"Incredients from Allergen: {tmpIncredients}")

        # check if elemAllergen is the only element with this count of existence
        erg = []
        for elem in tmpIncredients:
            tmpExist = True
            if elem == elemAllergen:
                continue
            for key, val in tmpDict.items ():
                if elem == elemAllergen:
                    continue
                if elem not in val:
                    tmpExist = False
                    break
            if tmpExist:
                erg.append(elem)
        print(f"{erg} is the only Incredient which exists in all food for {elemAllergen}")
        if len(erg) == 1:
            findSomething = True
            ingredientsList.remove(erg[0])
            print(f"IngredientsList New: {ingredientsList}")
            for key,val in ingredientsDict.items():
                if erg[0] in val:
                    ingredientsDict[key].remove(erg[0])
            # for key,val in ingredientsDict.items():
            #     print(key,val)
            ergResultList.append(erg[0])
    if not findSomething:
        break
# Count ingredients who are left over
countErg = 0
for key,val in ingredientsDict.items():
    countErg += len(val)
print(f"Final Result: {countErg}")















