"""6. Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso. Si
existe diferencia positiva entre este promedio de peso y el peso de la última
vez que se reunieron, significa que subieron de peso. Pero si la diferencia
es negativa, significa que bajaron. Lo que el problema requere es que por
cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
cantidad de kilos que subió o bajó de peso."""

fatBoy1 = float(input("Enter the first weight 1° fat boy: "))
fatBoy2 = float(input("Enter the first weight 2° fat boy: "))
fatBoy3 = float(input("Enter the first weight 3° fat boy: "))
fatBoy4 = float(input("Enter the first weight 4° fat boy: "))
fatBoy5 = float(input("Enter the first weight 5° fat boy: "))

fatBy1 = 0
fatBy2 = 0
fatBy3 = 0
fatBy4 = 0
fatBy5 = 0

for i in range(1,10):
	weight1 = float(input(f"Enter the {i + 1} weight of the first fat boy: "))
	fatBy1 = fatBy1 + weight1

	weight2 = float(input(f"Enter the {i + 1} weight of the second fat boy: "))
	fatBy2 = fatBy2 + weight2

	weight3 = float(input(f"Enter the {i + 1} weight of the third fat boy: "))
	fatBy3 = fatBy3 + weight3

	weight4 = float(input(f"Enter the {i + 1} weight of the fourth fat boy: "))
	fatBy4 = fatBy4 + weight4

	weight5 = float(input(f"Enter the {i + 1} weight of the fifth fat boy: "))
	fatBy5 = fatBy5 + weight5


def calculate_operation_fat(fat, fatb):
	avarage = (fat + fatb) / 3
	
	if avarage < fatb:
		print(f"You have down {fatb - avarage}")
	elif avarage > fatb:
		print(f"You have up {avarage - fatb}")
	else:
		print("You have stayed")

boyFat(fatBy1, fatBoy1)
boyFat(fatBy2, fatBoy2)
boyFat(fatBy3, fatBoy3)
boyFat(fatBy4, fatBoy4)
boyFat(fatBy5, fatBoy5)
