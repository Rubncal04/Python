"""10. La empresa Encuestas S.A desea crear una función que les permita
conocer de los 50.000 votos obtenidos por 3 candidatos, cual de estos fue
el ganador o indicar si hubo empate y la cantidad de votos obtenidos."""


candidate1 = 0
candidate2 = 0
candidate3 = 0


votes = 50

for i in range(votes):
    election = input("Select your favorite candidate. Mark 1, 2 or 3: ")

    if election == "1":
        candidate1 += 1
    elif election == "2":
        candidate2 += 1
    elif election == "3":
        candidate3 += 1
    else:
        print("Selection wrong. Please mark again")

def comparation(cand1,cand2,cand3):
    if cand1 > cand2 and cand1 > cand3:
        print(f"The winner is Candidate 1. Total votes: {cand1}")
    elif cand2 > cand1 and cand2 > cand3:
        print(f"The winner is Candidate 2. Total votes: {cand2}")
    elif cand3 > cand1 and cand3 > cand2:
        print(f"The winner is Candidate 3. Total votes: {cand3}")
    else:
        print("It had a draw.")

print(comparation(candidate1,candidate2,candidate3))
