# Q1
D={'Nom': 'Mbappé', 'Prénom': 'Killian'}
print(D)

# Q2
D['Age']=21
print(D)

# Q3
age_sup = D['Age']>len(D['Nom']+D['Prénom'])
print(age_sup)

# Q4
D2={'Adresse': "ici"}
D.update(D2)

print(D)

# Q5

D['AgeLycée'] =  16
del D['Age']

print(D)
# Q6
#---- copier coller - exo 1 ----
with open('emails.txt') as f:
    M = f.read().splitlines()

D = []
for adresse in M:
    s = adresse.split("@")
    domaine = s[1]
    D.append(domaine)
#---- fin : copier coller - exo 1 ----
D_dico = {}
for domaine in D:
    if domaine not in D_dico:
        D_dico[domaine] = 1
    else:
        D_dico[domaine] = D_dico[domaine] + 1
print(D_dico)
   
