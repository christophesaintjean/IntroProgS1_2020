# Nettoie un dictionnaire en eliminant toutes les cles dont la valeur est None


def clean_dict(D):
    for cle, valeur in D.items():
        if valeur is None:
            del D[cle]
    return D
        
def clean_dict_bis(D):
    D2 = D.copy()
    for cle, valeur in D2.items():
        if valeur is None:
            del D[cle]
    return D

D_eff = {'a': 2, 'b': None, 'c': None, 'd': 4}

print(clean_dict_bis(D_eff))



