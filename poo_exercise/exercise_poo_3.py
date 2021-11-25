"""
3. Programe una clase que permita crear un número complejo y realizar las
siguientes operaciones:
a. Sumar
b. Restar
c. Multiplicar
d. Dividir
"""

class ComplexNumber:
    """docstring for."""

    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    def __str__(self):
        return f"{self.real_num} + {self.imaginary_num}i"

    def get_real_num(self):
        return self.real_num

    def get_imaginary_num(self):
        return self.imaginary_num

    def sum(self, other_num):
        a = self.real_num + other_num.real_num
        b = self.imaginary_num + other_num.imaginary_num
        return ComplexNumber(a, b)

    def subtract(self, other_num):
        a = self.real_num - other_num.real_num
        b = self.imaginary_num - other_num.imaginary_num
        return ComplexNumber(a, b)

    def product(self, other_num):
        a = self.real_num * (other_num.real_num)
        b = self.real_num * (other_num.imaginary_num)
        c = self.imaginary_num * (other_num.real_num)
        d = self.imaginary_num * (other_num.imaginary_num)
        e = a + (d * -1)
        d = b + c
        return ComplexNumber(e, d)

    def division(self, other_num):
        a = self.real_num * other_num.real_num
        b = self.real_num * other_num.imaginary_num
        c = self.imaginary_num * other_num.real_num
        d = self.imaginary_num * other_num.imaginary_num
        denominator_1 = other_num.real_num ** 2
        denominator_2 = other_num.imaginary_num ** 2
        e = a + (d * -1)
        d = b + c
        f = denominator_1 + denominator_2
        return f"{e} / {f} + {d}i / {f}"


number_1 = ComplexNumber(4, 5)
number_2 = ComplexNumber(8, -2)
print(number_1.division(number_2))
