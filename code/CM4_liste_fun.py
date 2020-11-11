"""
Ecrire une fonction qui multiplie
chacun des éléments d'une liste par un nombre
version non place puis en place
"""
def mult_liste(L, c):
    L2 = []
    for x in L:
        L2.append(c * x)
    return L2

def mult_liste_en_place(L, c):
    for i, x in enumerate(L):
        L[i]  = c * x

L = [4, 3, 0, 2]

print(mult_liste(L, 2))

mult_liste_en_place(L, 2)
print(L)

"""
Generaliser à une fonction passée en paramètre
"""
def mult_par_2(x):
    return 2*x


def map_liste(L, fun):
    for i, x in enumerate(L):
        L[i]  = fun(x)

L = [4, 3, 0, 2]
map_liste(L, mult_par_2)
print(L)

"""
Exercice: Generaliser à une liste de fonctions passée en paramètre
f0 o f1 o .. o fp
"""