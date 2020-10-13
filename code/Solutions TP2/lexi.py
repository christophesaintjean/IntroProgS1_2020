prenom1 = input("Prénom 1 ? ")
prenom2 = input("Prénom 2 ? ")

if prenom1 < prenom2:
    print(f"{prenom1} < {prenom2}")
elif prenom1 > prenom2:
    print(f"{prenom2} < {prenom1}")
else:
    print(f"{prenom1}, {prenom2} sont égaux")