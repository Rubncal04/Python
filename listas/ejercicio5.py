"""5. Dado un Vector v de longitud par, divida en 2 partes, en la primera parte
realice la productoria y en la segunda la sumatoria. Entregue los valores
resultantes."""

from math import prod

listA = [1, 2, 4, 7, 8, 9, 6, 10, 5, 3]

sub_list = int(len(listA) / 2)

sub_list1 = sum(listA[:sub_list])
sub_list2 = prod(listA[sub_list:])

print(sub_list1)
print(sub_list2)
