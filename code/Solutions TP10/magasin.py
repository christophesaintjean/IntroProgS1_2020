d_pu = {
    "Épée en mousse": 5,
    "Masque Dark Vador": 30,
    "Hand spinner 3d": 10,
    "Console Minux": 150,
    "Lego Footix": 15
    }

d_stock = { 
    "Masque Dark Vador": 4,
    "Hand spinner 3d": 10,
    "Console Minux": 2,
    "Lego Footix": 5,
    "Épée en mousse": 10
    }


def verification(d1, d2):
    for k1 in d1.keys():
        if k1 not in d2:
            return False
    for k2 in d2.keys():
        if k2 not in d1:
            return False
    return True

def verification_2(d1, d2):
    return d1.keys() == d2.keys()

print(verification(d_pu, d_stock))

def achat_possible(k, v, d):
    return k in d and d[k]>=v

print(verification(d_pu, d_stock))
print(achat_possible("Hand spinner 3d", 2, d_stock))
print(achat_possible("Console Minux", 5, d_stock))

def achats_possibles(d_achats, d_stock):
    #for produit, quantite in d_achats.items():
    #    if not achat_possible(produit, quantite, d_stock):
    for produit in d_achats.keys():
        if not achat_possible(produit, d_achats[produit], d_stock):
            return False
    return True
        
print('*' * 10 + ' Achats possibles ' +  '*' * 10 )  
print(achats_possibles({"Hand spinner 3d": 2}, d_stock))
d_achats = {"Hand spinner 3d": 2, "Console Minux": 3}
print(achats_possibles(d_achats, d_stock))           
                