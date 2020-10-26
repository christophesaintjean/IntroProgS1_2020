min = 1
max = 5000

print(f"Début du jeu [{min}, {max}]")
print(19*'-')

cpt = 0
while True:
    print(f"[{min}, {max}]")
    prop = (min + max) // 2
    cpt = cpt + 1
    rep = input(f"Est ce {prop} ? ")
    if rep == "+":
        min = prop + 1
    elif rep == "-":
        max = prop - 1
    else:
        break
 
print(f"Tu avais choisi {prop}.")
print(f"en {cpt} coups.")
