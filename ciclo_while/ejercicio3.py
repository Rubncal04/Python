"""de los n elementos de la serie de fibonacci diga cuántos son impares
cuántos son impares y cuántos ceros"""

print("Serie Fibonacci")

n_elements = [2, 3, 7, 0, 6]
even = []
odd = []
cero = []

ended = False

while ended == False:

    for i in n_elements:

        if i == 0:
            cero.append(i)
        elif i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    ended = True

print(f"\nThese are even numbers: {even}")
print(f"These are odd numbers: {odd}")
print(f"These are cero numbers: {cero}")
