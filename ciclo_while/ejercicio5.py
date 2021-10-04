""" En 1994 el país A tiene una población de 25 millones de habitantes y el
país B de 19.9 millones. Las tasas de creción de población es del 2% y del 3%
respectivamente. Desarrollar un algoritmo para informar en qué año el país B
supera la del país A"""

countryA = 25
countryB = 19.9
year = 1994

while countryA > countryB:
    countryA = countryA + (countryA * 0.02)
    countryB = countryB + (countryB * 0.03)

    year +=1

print(f"Country A: {round(countryA, 1)}")
print(f"country B: {round(countryB, 1)}")
print(f"Year: {year}")
