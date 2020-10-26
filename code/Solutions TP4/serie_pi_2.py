import math

n = 100
som = 0

for k in range(n+1):
    som = som + (-3)**-k / (2*k+1)

print("Approximation de l'algorithme :", math.sqrt(12) * som)
print("Valeur système de math.pi", math.pi)

print('-'*10 + ' Recherche de la meilleure série ' + '-'*10)

erreur = 1e-6

print("-" * 10 + " Serie 2 (TP) "+ "-" * 10)

som = 0
k = 0
approx_pi = 0
python_pi = math.pi

while not math.isclose(approx_pi, python_pi, abs_tol=erreur):
    som = som + (-3) ** -k / (2 * k + 1)
    approx_pi = math.sqrt(12) * som
    k = k + 1
print(k, 'termes suffisent pour une approximation à',
      erreur, 'près!')

print("-" * 10 + " Serie 1 (CM) "+ "-" * 10)
som = 0
k = 0
approx_pi = 0

while not math.isclose(approx_pi, python_pi, abs_tol=erreur):
    som = som + (-1) ** k / (2 * k + 1)
    approx_pi = 4 * som
    k = k + 1
print(k, 'termes suffisent pour une approximation à',
      erreur, 'près!')
