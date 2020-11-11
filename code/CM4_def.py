from datetime import datetime
 
def bonjour():
    heure = datetime.now()
    print(f"Bonjour, il est {heure}")
 
def aff_somme_n_entiers(n):
    som = 0
    for i in range(1, n+1):
        som = som + i
    print(f"Résultat: {som}")
      
def aff_diff_ch(ch1, ch2):
    ch1_u = ch1.upper()
    ch2_u = ch2.upper()
    if ch1_u == ch2_u:
        print(f"{ch1} et {ch2} sont égales à la casse près")
    else:
        print(f"{ch1} et {ch2} sont différentes")
