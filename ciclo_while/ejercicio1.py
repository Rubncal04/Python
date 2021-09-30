""" de los n números primos contenidos en un intérvalo (por ejemplo los números primos
del 1 al 100) calcule la sumatoria y el promedio"""

list = []
count = 0

def is_prime(num):
    factors_count = 0

    for x in range(1, num + 1):
        if num % x == 0:
            factors_count += 1

    if factors_count == 2:
        return True
    else:
        return False

number = int(input("Enter a number: "))

while is_prime(number):
    list.append(number)
    number = int(input("Enter other number: "))

    count += 1

if is_prime(number) == False:
    print(f"\nThe number {number} isn't a prime number\n")

print(f"The sum of all numbers of the list is: {sum(list)}\n")
print(f"The avarage of all numbers of the list is: {sum(list) / count}")
