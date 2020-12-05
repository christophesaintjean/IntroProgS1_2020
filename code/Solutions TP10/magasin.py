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
    #return d[k]>=v and k in d
print(verification(d_pu, d_stock))
print(achat_possible("Hand spinner 3d", 2, d_stock))
print(achat_possible("Console Minux", 5, d_stock))

                
                