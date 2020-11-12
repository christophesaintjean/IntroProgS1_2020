"""
Ecrire une fonction qui multiplie
chacun des éléments d'une liste par un nombre
version en place puis non place
"""

def mult_en_place(L, c):
    for i in range(len(L)):
        L[i] = c * L[i]
    return L

def mult_copy(L, c):
    L2 = L.copy()  # L[:]
    for i in range(len(L2)):
        L2[i] = c * L2[i]
    return L2

def mult_append(L, c):
    L2 = []
    for i in range(len(L)):
        L2.append(c * L[i])
    return L2
    
A = [5, 2, -4, 0 , 1]
print(mult_copy(A, 2))
print(mult_append(A, 2))
print(mult_en_place(A, 2))

# Bonus composition de fonctions
print(mult_en_place(mult_en_place(A, 2), 1/2))
#mult_en_place(A, 2)
#mult_en_place(A, 1/2)

"""
Generaliser à une fonction passée en paramètre
"""
def mult_par_2(x):
    return 2 * x

def add_5(x):
    return x + 5

def map_liste(L, fun):
    for i in range(len(L)):
        L[i] = fun(L[i])
    return L

A = [5, 2, -4, 0 , 1]
print(map_liste(A, mult_par_2))
print(map_liste(A, add_5))
    

"""
Exercice: Generaliser à une liste de fonctions passée en paramètre
f0 o f1 o .. o fp
"""

def maps_liste(L, fun_list):
    ...
    return L

A = [5, 2, -4, 0 , 1]
maps_liste(A, [add_5, mult_par_2])
