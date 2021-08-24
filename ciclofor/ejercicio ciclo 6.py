"""6. Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso. Si
existe diferencia positiva entre este promedio de peso y el peso de la última
vez que se reunieron, significa que subieron de peso. Pero si la diferencia
es negativa, significa que bajaron. Lo que el problema requere es que por
cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
cantidad de kilos que subió o bajó de peso."""

first_weight = float(input("Enter the first weight: "))

final_weight = 0

for i in range(1, 3):
	weight = float(input(f"Enter the {i + 1}° weight: "))
	if weight > 0:
		final_weight = final_weight + weight
		

avarage = ((final_weight + first_weight) / 3)

if avarage < first_weight:
	print(f"You´re lost weight: {avarage - first_weight}")
else:
	print(f"You´re got weight: {avarage - first_weight}")