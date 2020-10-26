import random

min = 1
max = 20

print(f"Début du jeu [{min}, {max}]")
print(19*'-')   #   print("------------------------------")
x = random.randint(min, max)
prop = None

cpt = 0
while True:
    prop = int(input("Propose un nombre: "))
    cpt = cpt + 1
    if x < prop:
        print("Plus petit.")
    elif x > prop:
        print("Plus grand.")
    else:
        break

print(f"Bravo, j'avais choisi {prop}.")
print(f"en {cpt} coups.")