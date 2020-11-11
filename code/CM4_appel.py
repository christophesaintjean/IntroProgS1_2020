def somme_n_entiers(n):
    som = 0
    for i in range(1, n+1):
        som = som + i
    return som


res = somme_n_entiers(5)
print(res)

n =  10
print(somme_n_entiers(n))