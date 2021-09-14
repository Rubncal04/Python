"""4. De los n elementos de un vector dado identifique el número que mas se
repite e indique cual es."""

list = []
sames = []

rounds = 7

for i in range(rounds):
    numbers = int(input("Enter the number you want to add to the list: "))
    list.append(numbers)

for i in range(len(list)):
    for x in range(len(list)):
        if i != x:
            if list [i] == list[x] and list [i] not in sames:
                sames.append(list[i])

print(f"This is your list: {list}")
print(f"the sames numbers are: {sames}")
