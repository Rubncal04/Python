"""Teniendo como entrada un número entero, determinar cuántos dígitos tiene, cuántos de ellos son
pares e impares, calcule la sumatoria, la productoria y el promedio de estos"""

from math import prod
from random import randint

cont = 0
numbers = int(input("Enter a number: "))
print(numbers)

while numbers > 0:
    numbers //= 10
    cont += 1

print(cont)
print(f"The sum is: {cont + numbers}")
