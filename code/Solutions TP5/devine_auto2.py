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
    
    if prop < a_deviner:
        min = prop + 1
    elif prop > a_deviner:
        max = prop - 1
    else:
        break
print(f"Bravo, j'avais choisi {prop}.")
print(f"en {cpt} coups.")


