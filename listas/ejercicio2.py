"""2. De los n elementos de un vector dado calcule:
a. Cantidad de elementos pares
b. Cantidad de elementos impares
c. Cantidad de elementos primos"""

numberUser = int(input("Enter the numbers you want: "))
even = []
odd = []
prime = []
list = []

for i in range(numberUser):
    numbers = int(input(f"Enter the {i + 1}° number: "))
    list.append(numbers)
    if numbers % 2 == 0:
        even.append(numbers)

    elif numbers % 2 != 0:
        odd.append(numbers)

print(f"Your list is: {list}")
print(f"These are your even numbers: {even}")
print(f"The odd numbers are: {odd}")
