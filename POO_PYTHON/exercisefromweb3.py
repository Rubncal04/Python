"""Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y
la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Construye
los siguientes métodos para la clase:
1. Un constructor.
2. Los setters y getters para el nuevo atributo.
3. En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo
tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor de edad
pero menor de 25 años y falso en caso contrario.
4. Además la retirada de dinero sólo se podrá hacer si el titular es válido.
5. El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
* Piensa los métodos heredados de la clase madre que hay que reescribir."""

class Account():
    def __init__(self, owner):
        self.__owner = owner
        self.__number_account = "00890334"
        self.__saved_money = 0

    def putting_money(self, putMoney):
        if put_money < 0:
            return "Please, Enter a positive value"
        else:
            self.__saved_money += putMoney
            return {self.__saved_money}

    def withdraw_money(self, withdraw):
        self.__saved_money -= withdraw
        return f"money saved:  ${self.__saved_money}"

    def show(self):
        print(f"\nPersonal information\nUser: {self.__owner}\nNumber account: {self.__number_account}")


class Account_young(Account):

    def __init__(self):

        super().__init__(user)

        self.__age = 0
        self.__bonus = 5

    def age_young(self, age):
        self.__age = age
        return self.__age

    def elder(self):
        self.young_elder = False
        if self.__age >= 18 and self.__age < 25:
            self.young_elder = True
            return self.young_elder
        else:
            return self.young_elder

    def bonus_card(self):
        self.__bonus = self.saved_money * 0.5
        return self.__bonus

    def show(self):
        if self.young_elder == True:
            super().show()
            print(self.__bonus)
        else:
            print("You're not avaliabled")


user = input("Enter your Username: ")
put_money = int(input("How many money do you want to save? "))
withdraw = int(input("withdraw money: "))
age = int(input("Enter your age: "))

#person1 = Account(user)
#person1.show()
#person1.putting_money(put_money)
#print(person1.withdraw_money(withdraw))
young = Account_young()
young.age_young(age)
young.elder()
young.show()
print(isinstance(young, Account))
