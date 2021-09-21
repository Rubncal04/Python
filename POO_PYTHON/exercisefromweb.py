"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""


class People():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.dni = 0

    def obtening(self, name, age, dni):
            self.name = name
            self.age = age
            self.dni = dni

    def isElder(self):
        if (self.age) > 18:
            return "You are elder."
        else:
            return "you are so young"

    def show(self):
        print(f"Your personal information is:\nname: {self.name.capitalize()}\nage: {self.age}\nDNI: {self.dni}")

Name = input("What's your name? ")
Age = int(input("Enter your age: "))
Dni = int(input("Enter your number identification: "))

person1 = People()
person1.obtening(Name, Age, Dni)
person1.show()
print("\n",person1.isElder())
