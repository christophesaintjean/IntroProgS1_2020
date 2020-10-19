for i in range(1, 6):
    print(i, end=" ")
print()


a = int(input("a ? "))
b = int(input("b ? "))

prod = 0
if b < a:
    for i in range(b):
        prod = prod + a
else:
    for i in range(a):
        prod = prod + b
        
print(f"{prod} est {a*b} {prod == a*b}")



