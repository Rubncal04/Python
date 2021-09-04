"""Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
las siguientes operaciones:
a. Suma
b. Resta"""

import itertools

listA = []
listB = []

def subtraction(a, b):
    print(f"The subtraction is: {a - b}")

for i in range(7):
    listOne = int(input("Choose 7 numbers for the first list: "))
    listA.append(listOne)

    listTwo = int(input("Choose 7 numbers for the second list: "))
    listB.append(listTwo)

listC = list(itertools.chain(listA, listB))
print("-------------------------------------------------")

print(f"This is the first list: {listA}\n")
print(f"This is the second list: {listB} \n")
print(f"The sum of all numbers of the lists are: {sum(listC)}\n")
subtraction(sum(listA), sum(listB))
