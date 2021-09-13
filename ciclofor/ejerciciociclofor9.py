"""9. Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
siguiente tabla:
Valor vendido Comisión
Menor o igual que 20 Millones = 10%
Mayor de 20 Millones y menor de 40 Millones = 15%
Mayor o igual de 40 Millones y menor de 80 Millones = 20%
Mayor o igual de 80 millones y menor de 160 Millones = 25%
De 160 Millones en adelante = 30%
Realice un método que diga cuanto vendió y la comisión de los 100
vendedores que tiene la empresa"""


sellers = 100

for i in range(sellers):
	sale = float(input(f"Enter the sale of the {i + 1}° sellers: "))

	if sale <= 20:
		print(f"His sale is {sale} and his comision is {sale * 0.10}")
	elif sale > 20 or sale < 40:
		print(f"His sale is {sale} and his comision is {sale * 0.15}")
	elif sale >= 40 or sale < 80:
		print(f"His sale is {sale} and his comision is {sale * 0.20} ")
	elif sale >= 80 or sale < 160:
		print(f"His sale is {sale} and his comision is {sale * 0.25}")
	elif sale >= 160:
		print(f"His sale is {sale} and his comision is {sale * 0.30}")
