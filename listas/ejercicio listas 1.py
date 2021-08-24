""" 1. de los elementos n de un vector dado, calcule:
a: la sumatoria
b: la productoria
c: el mayor elemento
d: el menor elemento"""
from math import prod

rounds = 6
highest = int(input("Enter the first number: "))
numbers = [highest]
smallest = highest

for i in range(1,rounds):
	number = int(input(f"Enter the {i + 1}° number: "))
	numbers.append(number)

	if numbers[i] < smallest:
		smallest = numbers[i]

	if numbers[i] > highest:
		highest = numbers[i] 	

print(f"These are all your list: {numbers[:]}")
print(f"the highest number is: {highest}")
print(f"the smallest number is: {smallest}")
print(f"The sum of all numbers is: {sum(numbers)}")
print(f"The product is: {prod(numbers)}")
