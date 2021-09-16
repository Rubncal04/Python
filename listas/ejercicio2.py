"""2. De los n elementos de un vector dado calcule:
a. Cantidad de elementos pares
b. Cantidad de elementos impares
c. Cantidad de elementos primos"""

numberUser = int(input("How many numbers do you want to know about its logic? "))
even = []
odd = []
prime = []
list = []

def is_prime(num):
    factors_count = 0

    for x in range(1, num + 1):
        if num % x == 0:
            factors_count += 1

    if factors_count == 2:
        return True
    else:
        return False

for i in range(numberUser):
    numbers = int(input(f"Enter the {i + 1}° number: "))
    list.append(numbers)
    if numbers % 2 == 0:
        even.append(numbers)
    else:
        odd.append(numbers)

    if is_prime(numbers):
        prime.append(numbers)

print(f"Your list is: {list}\n")
print(f"These are your even numbers: {even}\n")
print(f"The odd numbers are: {odd}\n")
print(f"These are numbers prime: {prime}")
