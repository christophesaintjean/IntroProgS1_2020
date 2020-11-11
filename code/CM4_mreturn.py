def prenom_nom(ch):
    lch = ch.split(" ")
    return {"Prénom":lch[0], "Nom":lch[1]}

print(prenom_nom("Atahualpa Yupanqui"))
