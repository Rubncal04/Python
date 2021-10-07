"""Crea una tupla con los meses del año, pide números al usuario, si el numero
esta entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición
sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero."""

print("Choose the month what you want\n")

months_year = ("January", "Febrary", "March", "April", "May", "June", "July", "August",\
               "September", "Octuber", "November", "Dicember")

number_of_user = int(input("Enter a number: "))

while number_of_user > 0:
    for i in range(len(months_year)):

        if number_of_user > 0 and number_of_user <= i + 1:
            print(f"This month you've selected: {months_year[number_of_user - 1]}\n")
            
            number_of_user = int(input("Enter a number: "))

print("There was an error")
