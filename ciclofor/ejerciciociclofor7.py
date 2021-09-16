"""7. En un supermercado una ama de casa pone en su carrito los artículos que
va tomando de los estantes. La señora quiere asegurarse de que el cajero
le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
artículo anota su precio junto con la cantidad de artículos iguales que ha
tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
que irá gastando en los demás artículos, hasta que decide que ya tomó
todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
compra."""

nProducts = int(input("How many different products do you want to buy? "))
grand_total = 0

for i in range(nProducts):
    product = int(input("How many of these? "))
    cost = int(input("How much it costs in Dollars? "))
    sub_total = cost * product
    grand_total = grand_total + sub_total

print(f"\nYou have spent {grand_total} Dollars")
