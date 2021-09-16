"""Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
las siguientes operaciones:
a. Suma
b. Resta"""

listA = []
listB = []
list3 = []
list4 = []

for i in range(6):
    list1 = int(input("Enter one number for the first list: "))
    listA.append(list1)
    list2 = int(input("Enter one number for the second list: "))
    listB.append(list2)

for i in range(len(listA)):
    list3.append(listA[i] + listB[i])
    list4.append(listA[i] - listB[i])

print(list3)
print(list4)
