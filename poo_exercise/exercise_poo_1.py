"""
1.Programe una clase que permite crear un número Fraccionario y realizar las
siguiente operaciones:
a.Sumar
b.Restar
c.Multiplicación
d.División
e.Convertir a un número Mixto
"""


class Fraction():
    """Create a fraction number"""

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        return f'{self.numerator}/{self.denominator}'

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def sum(self, other_fraction):
        if other_fraction.denominator == self.denominator:
            return Fraction(self.numerator + other_fraction.numerator,
                            self.denominator)
        else:
            a = self.numerator * other_fraction.denominator
            b = other_fraction.numerator * self.denominator
            c = self.denominator * other_fraction.denominator
            return Fraction(a + b, c)

    def subtract(self, other_fraction):
        if other_fraction.denominator == self.denominator:
            return Fraction(self.numerator - other_fraction.numerator,
                            self.denominator)
        else:
            a = self.numerator * other_fraction.denominator
            b = other_fraction.numerator * self.denominator
            c = self.denominator * other_fraction.denominator
            return Fraction(a - b, c)

    def product(self, other_fraction):
        return Fraction(self.numerator * other_fraction.numerator,
                        self.denominator * other_fraction.denominator)

    def divide(self, other_fraction):
        return Fraction(self.numerator * other_fraction.denominator,
                        self.denominator * other_fraction.numerator)

    def mixed_number(self):
        cocient = self.numerator // self.denominator
        result = self.numerator % self.denominator
        print(cocient, Fraction(result, self.denominator).display())


number = Fraction(6, 4)
number2 = Fraction(8, 5)
print(number.sum(number2).display())
# print(number.subtract(number2).display())
# print(number.set_fraction(), number2.set_fraction())
# number.mixed_number()
# print(number.product(number2).display())
# print(number.divide(number2).display())
