def f(x):
    x = x * 2
    print(x)
    
a = 2
f(a)


def f_liste(liste):
    print(id(liste))
    liste.append(1000)

L = [2, -1, 3]
f_liste(L)

