"""6. Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso. Si
existe diferencia positiva entre este promedio de peso y el peso de la última
vez que se reunieron, significa que subieron de peso. Pero si la diferencia
es negativa, significa que bajaron. Lo que el problema requere es que por
cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
cantidad de kilos que subió o bajó de peso."""

fatBoys = 5
fatBoy1 = []
cont = 0
cont2 = 0

for i in range(5):
	if cont2 < 5:
		for x in range(i):
			while cont < 10:
				weight = float(input("Enter the first weight: "))
				fatBoy1.append(weight)
				cont += 1
				break;
	cont2 +=
print(fatBoy1)
