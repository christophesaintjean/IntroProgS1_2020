L = [4, -2, 1, 3, 5]

print(f"Premier élément : {L[0]}, {L[-5]}")
print(f"Dernier élément : {L[4]}, {L[-1]}")

L[1] = 0
L[3] = L[2] + L[4]

print(L)

aux = L[0]
L[0] = L[1]
L[1] = aux

print(L)

L[1], L[0] = (L[0], L[1])

print(L)

L.remove(0)

print(L)