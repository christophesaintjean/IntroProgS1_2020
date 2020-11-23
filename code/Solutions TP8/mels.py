# Q.1
with open('emails.txt') as f:
    M = f.read().splitlines()

# Q.2
print(f"Adresses méls :{len(M)}", M, sep="\n")

# Q.3
i_max = 0
for i in range(len(M)):
    if len(M[i]) > len(M[i_max]):
        i_max = i
print(f"Max: {M[i_max]} à l'indice {i_max}")

# Q.4
D = []
for adresse in M:
    s = adresse.split("@")
    domaine = s[1]
    D.append(domaine)
print(D)

# Q.5
Du = []
for adresse in M:
    s = adresse.split("@")
    domaine = s[1]
    if domaine not in Du:
        Du.append(domaine)
    else:
        pass     # je n'ajoute pas car déjà connu
print(Du)

# Q.6
# Version 1 : naïve avec double boucle
for domaine_u in Du:
    cpt_u = 0
    for domaine in D:
        if domaine == domaine_u:
            cpt_u = cpt_u + 1
    print(f"{domaine_u} : {cpt_u} adresses")

# Version 2 : simple boucle plus efficace
domaine_prec = None
for domaine in D:
    if domaine_prec is None:
        cpt = 1
        domaine_prec = domaine
    elif domaine == domaine_prec:
        cpt = cpt + 1
    else:
        print(f"{domaine_prec} : {cpt} adresses")
        cpt = 1
        domaine_prec = domaine
print(f"{domaine_prec} : {cpt} adresses")
        

# Q.7


# Version 1 : idem à la version 1 de Q.6
Dn = []
for domaine_u in Du:
    cpt_u = 0
    for domaine in D:
        if domaine == domaine_u:
            cpt_u = cpt_u + 1
    Dn.append((domaine_u, cpt_u))
print(Dn)

# Version 2 : idem à la version 2 de Q.6
Dn = []
domaine_prec = None
for domaine in D:
    if domaine_prec is None:
        cpt = 1
        domaine_prec = domaine
    elif domaine == domaine_prec:
        cpt = cpt + 1
    else:
        Dn.append((domaine_prec, cpt))
        cpt = 1
        domaine_prec = domaine
Dn.append((domaine_prec, cpt))
print(Dn)

# Version 3 : voir exercice suivant sur les dicos.

    



