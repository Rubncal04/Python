"""3. Una empresa se requiere calcular el salario semanal de cada uno de los n
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de
las primeras 40 horas y $25 por cada hora extra"""

print("checking the salary of a worker")

workers = int(input("enter the number of workers: "))

basic_salary = 20

for i in range(workers):
	while True:
		time_work = int(input(f"enter the time of work {i+1}: "))
		if time_work <= 0:
			print("Enter error. Write again.")
		else:
			break;

	if time_work <= 40:
		print(f"salary of the {i + 1} worker is $ {basic_salary * time_work}")
	else:
		extra_time = time_work - 40
		print(f"Salary of the {i + 1} worker is $ {(basic_salary * 40) + (extra_time * 25)}")		


print("Thank you for using")