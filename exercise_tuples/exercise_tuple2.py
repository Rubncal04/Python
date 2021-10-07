"""Crea una tupla con números, pide un numero por teclado e indica cuantas veces se repite."""

tuple_of_numbers = (1, 3, 5, 79, 9, 45, 9, 76, 10, 34, 6, 5, 8, 1, 3, 4)

number = int(input("Enter a number: "))

print(f"the number {number} is {tuple_of_numbers.count(number)} times")
