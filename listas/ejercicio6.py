"""6. Dado un vector v, indique si es simétrico, un vector es simétrico si siendo
longitud par los números de la primera mitad son iguales al inverso de la
otra mitad por ejemplo: X=[1,2,3,3,2,1], en el ejemplo x es un vector
simétrico, en caso que la longitud del vector sea impar, se ignorará el
elemento central y se seguirá la misma lógica anterior, por ejemplo:
Y=[3,5,7,8,7,5,3], en este ejemplo Y es simétrico."""

import math

ask = int(input("How many numbers do you want to enter: "))

x = []

for i in range(1, ask + 1):
    number = int(input(f"Enter the {i}° number for your list: "))
    x.append(number)
    if i % 2 == 0:
        x1 = int(math.floor(len(x) / 2))
        y = x[:x1]
        z = x[x1:]
    elif i % 2 != 0:
        x1 = int(math.floor(len(x) / 2))
        y = x[:x1]
        z = x[x1+1:]

def exchange():
    count = 0
    for n in range(math.floor(len(z) / 2)):
        count -= 1
        z[n], z[count] = z[count], z[n]
    return z

if y == exchange():
    print(f"They are the sames {y} and {z}")
else:
    print("They aren't sames")
