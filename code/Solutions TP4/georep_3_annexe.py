## Annexe sur differents styles pour retrouver m

k = int(input("k ? "))


# première version (style 1): parcours ordre decroissant 
m = 179
while m >= 91:
    if k*360 % m == 0:
        break
    m = m - 1
print(m)


# première version (style 2): parcours ordre inverse 
# plus beau mais ne suppose pas que m existe
i = 179
while i >= 91:
    if k*360 % i == 0:
        m = i
        break
    i = i - 1
else:
    m = None 
    
if m is None:
    print("Pas de solution dans [91, 179]")
else:
    print(m)

# premiere version (bis) avec for: parcours ordre decroissant
for i in range(179, 90, -1):
    if k*360 % i == 0:
        m = i
        break
else:
    m = None
    
if m is None:
    print("Pas de solution dans [91, 179]")
else:
    print(m)
    
# deuxieme version: parcours ordre croissant
i = 91
m = None
while i < 179:
    if k*360 % i == 0:
        m = i
    i = i + 1
    
if m is None:
    print("Pas de solution dans [91, 179]")
else:
    print(m)
    
# deuxieme version bis avec for: parcours ordre croissant
m = None
for i in range(91, 180):
    if k*360 % i == 0:
        m = i
if m is None:
    print("Pas de solution dans [91, 179]")
else:
    print(m)
    
    
    