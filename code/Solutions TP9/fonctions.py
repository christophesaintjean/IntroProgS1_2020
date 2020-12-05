# definitions de fonctions

def aire_carre(cote):
    aire = cote * cote
    return aire


def aire_rectangle(hauteur, largeur):
    aire = hauteur * largeur
    return aire

def aire_carre2(cote):
    aire = aire_rectangle(cote, cote)
    return aire

def aire_rectangle2(hauteur, largeur=None):
    if largeur is None or largeur == hauteur:
        aire = aire_carre(hauteur)
    else:
        aire = hauteur * largeur
    return aire
    
def coords_carre(cote, x0y0):
    x0, y0 = x0y0
    L = [(x0, y0)]
    L.append((x0+cote, y0))
    L.append((x0+cote, y0+cote))
    L.append((x0, y0+cote))
    return L
    
# appel de fonctions
print(aire_carre(4))
print(aire_rectangle(3, 2))
print(aire_carre2(4))
print(aire_rectangle2(4, 2))
print(aire_rectangle2(4, 4))
print(aire_rectangle2(4))
print(coords_carre(1, (0, 0)))
print(coords_carre(4, (-2, 3)))


