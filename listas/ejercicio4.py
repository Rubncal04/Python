"""4. De los n elementos de un vector dado identifique el número que mas se
repite e indique cual es."""

list = []
sames = []

rounds = 7

for i in range(rounds):
    numbers = int(input("Enter the number you want to add to the list: "))
    list.append(numbers)
    most_repeated_number = list[0]

for i in range(len(list)):
    for x in range(len(list)):
        if i != x:
            if list[i] == list[x] and list[i] not in sames:
                sames.append(list[i])
                if list.count(list[i]) > list.count(most_repeated_number):
                    most_repeated_number = list[i]

if list.count(most_repeated_number) > 1:
    print(f"The number most repeated is: {most_repeated_number}")
else:
    print("There's no number repeated")

print(f"This is your list: {list}")
print(f"the sames numbers are: {sames}")
