import math

min = 1
max = 1000000


max_cpt = 0
sum_cpt = 0
for a_deviner in range(min, max+1):
    cpt = 0
    mini = min
    maxi = max
    while True:
        prop = (mini + maxi) // 2
        cpt = cpt + 1
        if prop < a_deviner:
            mini = prop + 1
        elif prop > a_deviner:
            maxi = prop - 1
        else:
            break
    sum_cpt = sum_cpt + cpt
    if cpt > max_cpt:
        max_cpt = cpt
    
print(f"Intervalle [{min}, {max}] :")
print(f"moyenne = {sum_cpt/(max-min+1)}, maximum = {max_cpt}")
print(f"log2(max-min+1) =  {math.log(max-min+1, 2)}")



