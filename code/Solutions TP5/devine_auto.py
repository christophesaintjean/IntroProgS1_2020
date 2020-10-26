min = 1
max = 1000000

print(f"Début du jeu [{min}, {max}]")
print(19*'-')

a_deviner = int(input(f"Quel est le nombre ?"))

cpt = 0
while True:
    print(f"[{min}, {max}]")
    prop = (min + max) // 2
    cpt = cpt + 1
    # version ou on remplacer la reponse à la question
    if prop < a_deviner:
        x = "+"
    elif prop > a_deviner:
        x = "-"
    else:
        x = "="  
        
    if x == "+":
        min = prop + 1
    elif x == "-":
        max = prop - 1
    else:
        break
print(f"Bravo, j'avais choisi {prop}.")
print(f"en {cpt} coups.")

