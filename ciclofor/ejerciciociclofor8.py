"""8. Un teatro otorga descuentos según la edad del cliente, determinar la
cantidad del dinero que el teatro deja de percibir por cada ua de las
categorias. Tomar en cuenta que los niños menores de 5 años no pueden
entrar al teatro y que existe un precio único en los asientos. Los descuentos
se hacen tomando en cuenta el siguiente cuadro:
Edad % Descuento
5 – 14 35%
15-19 25%
20 – 45 10%
46 – 65 25%
66 en Adelante 35%"""

print("Descuentos por categorías\ncategoría A 35%: De 5 a 14 años\ncategoría B 25%: De 15 a 19 años\ncategoría C 10%: De 20 a 45 años\ncategoría D 25%: De 46 a 65 años\ncategoría E 35%: De 66 en adelante")

valor_boleta = 12000
categoriaA = 0
categoriaB = 0
categoriaC = 0
categoriaD = 0
categoriaE = 0

participantes = int(input("Ingrese la cantidad de participantes: "))

for i in range(participantes):
	age = int(input(f"Ingrese la edad del participante {i + 1}: "))
	while age < 5:
		print("The child doesn't enter here")
		age = int(input(f"Ingrese la edad del participante {i + 1}: "))

	if age == 5 or age < 15:
		descuento1 = valor_boleta * 0.35
		categoriaA = categoriaA + descuento1
	elif age < 20:
		descuento2 = valor_boleta * 0.25
		categoriaB = categoriaB + descuento2
	elif age < 46:
		descuento3 = valor_boleta * 0.10
		categoriaC = categoriaC + descuento3
	elif age < 66:
		descuento4 = valor_boleta * 0.25
		categoriaD = categoriaD + descuento4
	elif age >= 66:
		descuento5 = valor_boleta * 0.35
		categoriaE = categoriaE + descuento5
	else:
		print("Ha ingresado una edad equivocada")


print(f"El total de perdida por la categoria A es: ${categoriaA}")
print(f"El total de perdida por la categoria B es: ${categoriaB}")
print(f"El total de perdida por la categoria C es: ${categoriaC}")
print(f"El total de perdida por la categoria D es: ${categoriaD}")
print(f"El total de perdida por la categoria E es: ${categoriaE}")
