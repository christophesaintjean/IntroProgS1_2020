desi = input("Désignation ? ")

pu = input("Prix unitaire ? ")
pu = float(pu)

quant = int(input("Quantité ? "))

prix = pu * quant

# trois façons de faire
print("Facture :", quant, desi, "à", pu, "€ l'unité font", prix, "€", sep =" ")
# equivalent à
#print("Facture :" + " " + str(quant) + " " + desi + " " + "à" + ...)
print("Facture : {} {} à {} € l'unité font {} €".format(quant, desi, pu, prix))
# version recommandée
print(f"Facture : {quant} {desi} à {pu} € l'unité font {prix} €")