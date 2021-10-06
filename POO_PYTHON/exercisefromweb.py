"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""


class Person():
    def __init__(self, name, age, dni):
        self.__name = name
        self.__age = age
        self.__dni = dni

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__name = age

    def set_dni(self, dni):
        self.__dni = dni

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_dni(self):
        return self.__dni

    def is_elder(self):
        if (self.__age) > 18:
            return "You are elder."
        else:
            return "you are so young"

    def show(self):
        print(f"Your personal information is:\nName: {self.__name.capitalize()}\
              \nAge: {self.__age}\nDNI: {self.__dni}")

name = input("What's your name? ")
age = int(input("Enter your age: "))
dni = int(input("Enter your identification number: "))

person1 = Person(name, age, dni)
#person1.show()
#person1.set_name("Ruben")
#person1.show()
print("\n",person1.is_elder())
