i = 1
while i <= 5:  
    print(i, end=" ")
    i = i + 1
print()

# Parcours explicite des nombres pairs
i = 2
while i <= 12:
    print(i, end=" ")
    i = i + 2
print()

# Parcours de tous les nombres + test de parite
i = 2
while i <= 12:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1
print()

# Parcours explicite des nombres pairs
i = 4
while i <= 20:
    print(i, end=" ")
    i = i + 2
print()

# Parcours de tous les nombres + test de parite
i = 3
while i <= 21:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1
print()

# 10 multiples de 5, par ordre décroissant
# et en commençant à 130.

i = 130
cpt = 0
while cpt < 10:
    if i % 5 == 0:
        print(i, end=" ")
        cpt = cpt + 1  
    i = i - 1




    