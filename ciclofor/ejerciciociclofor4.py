"""4. Calcular el promedio de edades de hombres, mujeres y de todo un grupo
de alumnos."""

print("Average age of students")

students = int(input("Enter the number of students: "))
ages_students = 0

for i in range(students):
	age = int(input(f"Enter age of the {i + 1}° student: "))

	if age > 0:
		ages_students = ages_students + age

print(f"The average age of students is {ages_students / students} ")
