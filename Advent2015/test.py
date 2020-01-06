import copy
liste = [['.', '#', '.', '#', '.', '#'], ['.', '.', '.', '#', '#', '.']]
print(liste)
temp_liste = copy.deepcopy(liste)
temp_liste[0][2] = '!'
print(temp_liste)
print(liste)

num1 = [[1,2,3,4,5]]
num2 = copy.deepcopy(num1)
num2[0][2] = 9
print(num1)
print(num2)














