"""5. Encontrar el menor valor de un conjunto de n números dados"""

n = int(input("Enter the quantity numbers: "))
smallest_num = float(input("Enter the first number: "))

for i in range(1, n):
	num = float(input("Enter the fallowing number: "))

	if num < smallest_num:
		smallest_num = num

print(f"The smallest number is {smallest_num}")
