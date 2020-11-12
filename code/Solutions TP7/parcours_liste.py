import random

R = []

for i in range(10):
    alea = random.randint(1, 20)
    R.append(alea)
    
long = len(R)

print("[", end="")
for i in range(long):
    print(R[i], end=": ")
print(f"]")

print("[", end="")
for Ri in R:
    print(Ri, end=": ")
print(f"]")

somme = 0
for Ri in R:
    somme = somme + Ri
print(f"Somme = {somme}")

i_max = 0
for i in range(1, long):
    if R[i] > R[i_max]:
        i_max = i
print(f"Position du max = {i_max}, max = {R[i_max]}")
    
cpt = 0
for Ri in R:
    if Ri >= 10:
        cpt = cpt + 1
print(f"Nbre de valeurs >= 10 : {cpt}")

R2 = []
for Ri in R:
    if Ri > 10:
        R2.append(-Ri)
    else:
        R2.append(Ri)
print(R2)

R3 = R + R2
print(R3)


    
    
    
    
    
    
    
    
    
    
    
    
    