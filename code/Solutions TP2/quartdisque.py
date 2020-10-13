x = float(input("x ? "))
y = float(input("y ? "))

C_x01 = (x >= 0) and (x <= 1)
C_y01 = 0 <= y <= 1
C_disque = x**2 + y**2 <= 1



if C_x01 and C_y01 and C_disque:
    print(f"Le point ({x}, {y}) est dans le quart de disque sup. droit")
else:
    print(f"Le point ({x}, {y}) n'est pas dans le quart de disque sup. droit")
    
if C_disque and x >= 0 and y >= 0:
    print(f"Le point ({x}, {y}) est dans le quart de disque sup. droit")
else:
    print(f"Le point ({x}, {y}) n'est pas dans le quart de disque sup. droit")