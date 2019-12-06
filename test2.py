import csv

def readlist (filename):
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=",")
        return(list(csv_reader))

liste1 = readlist("Advent03_liste1.csv")
liste2 = readlist("Advent03_liste2.csv")

print(liste1)