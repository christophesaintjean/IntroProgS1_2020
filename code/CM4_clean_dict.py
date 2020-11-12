# Nettoie un dictionnaire en eliminant toutes les cles dont la valeur est None

D = {'a': 2, 'b': None, 'c': None, 'd': 4}

def clear_dict(D_formel):
    for cle, valeur in D_formel.items():
        if valeur is None:
            del D_formel[cle]
            
def clear_dict_copy(D_formel):
    D_local = D_formel.copy()
    for cle, valeur in D_local.items():
        if valeur is None:
            del D_formel[cle]

clear_dict_copy(D)

#print(clean_dict_bis(D_eff))



