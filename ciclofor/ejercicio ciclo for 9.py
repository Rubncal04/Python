"""9. Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
siguiente tabla:
Valor vendido Comisión
Menor o igual que 20 Millones = 10%
Mayor de 20 Millones y menor de 40 Millones = 15%
Mayor o igual de 40 = 20%"""


sellers = 100

for i in range(sellers):
	sale = float(input(f"Enter the sale of the {i + 1}° sellers: "))

	if sale <= 20000000:
		print(f"The comision of the sellers is {sale + (sale * 0.10)}")
	elif sale < 40000000:
		print(f"The comision of the seller is {sale +(sale * 0.15)}")
	elif sale >= 40000000 or sale < 80000000:
		print(f"The comision of the seller is {sale + (sale * 0.20)} ")
	elif sale >= 80000000 or sale < 160000000:
		print(f"The comision of the seller is {sale + (sale * 0.25)}")
	elif sale > 160000000:
		print(f"The comision of the seller is {sale + (sale * 0.30)}")