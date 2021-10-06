"""de los n elementos de la serie de fibonacci diga cuántos son impares
cuántos son impares y cuántos ceros"""

print("Serie Fibonacci")

number = int(input("Enter, how many time do you want to count the numbers: "))

even = []
odd = []
cero = []
count = 1
aux = 0

while number > 0:
    fbn = aux + count
    aux = count
    count = fbn
    print(fbn)
    if fbn % 2 == 0:
        even.append(fbn)
    else:
        odd.append(fbn)

    number -=1

print(f"\nThese are even numbers: {even}")
print(f"These are odd numbers: {odd}")
