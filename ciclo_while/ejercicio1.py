""" de los n números primos contenidos en un intérvalo (por ejemplo los números primos
del 1 al 100) calcule la sumatoria y el promedio"""

from random import randint
from math import prod

cont = 0
list = []
while cont < 10:
    numbers = randint(1,100)
    list.append(numbers)
    print(list)
    cont += 1

print()
if cont == 10:
    print(f"The sum of all numbers is: {sum(list)}\n")
    print(f"The product of all numbers is: {prod(list)}\n")
    print(f"The avarage is: {sum(list) / 10}")
