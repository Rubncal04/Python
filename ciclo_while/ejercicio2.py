"""Teniendo como entrada un número entero, determinar cuántos dígitos tiene, cuántos de ellos son
pares e impares, calcule la sumatoria, la productoria y el promedio de estos"""

from math import prod

number = input("Enter a integer number: ")

digits = []
even = []
odd = []
count = 1

def digits_of_numbers(number): #esta función me separa los dígitos de cada número y los ubica en una lista para así poder utilizarla

    ended = False
    list = []

    while ended == False:
        digit = int(number) % 10
        list.append(digit)

        if int(number) < 10:
            ended = True
        else:
            number = int(number) // 10
    return list

while count > 0:

    for i in range(len(number)): #este for me determina los dígitos que tiene el número
        digits.append(int(i + 1))

    for x in digits_of_numbers(number): #este for me indica a qué grupo pertenece cada número
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    count -= 1

print(f"\nThere is {digits[-1: ]} digits")
print(f"These are the even numbers: {even}")
print(f"These are the odd numbers: {odd}")
print(f"The sum of all numbers is: {sum(digits_of_numbers(number))}")
print(f"The product of all numbers is: {prod(digits_of_numbers(number))}")
