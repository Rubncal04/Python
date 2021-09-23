"""Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular
(que es una persona) y cantidad (puede tener decimales). El titular será obligatorio
y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
1.Los setters y getters para cada uno de los atributos. El atributo no se puede
modificar directamente, sólo ingresando o retirando dinero.
2.mostrar(): Muestra los datos de la cuenta.
3.ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida
es negativa, no se hará nada.
4.retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

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
            return f"You've saved:  ${self.__saved_money}"

    def withdraw_money(self, withdraw):
        self.__saved_money -= withdraw
        return f"Saved money: {self.__saved_money}"

    def show(self):
        print(f"\nPersonal information\nUser: {self.__owner}\nNumber account: {self.__number_account}")


user = input("Enter your Username: ")
put_money = int(input("How many money do you want to save? "))
withdraw = int(input("withdraw money: "))

person1 = Account(user)
person1.putting_money(put_money)
person1.show()
print(person1.withdraw_money(withdraw))
