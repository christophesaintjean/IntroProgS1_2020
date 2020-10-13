import math

x = float(input("x ? "))

if x >= 0:
    rac_x = math.sqrt(x)
    print(f"La racine carrée de {x} est {rac_x}")
else:
    print(f"Impossible de calculer la racine carrée de {x} qui est négatif")