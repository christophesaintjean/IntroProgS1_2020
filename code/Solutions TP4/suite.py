u0 = float(input("u0 ? "))
r = float(input("r  ? "))
n = int(input("n  ? "))

n_ = 0
u = u0
print(f"Les {n} premiers termes sont:")
while n_ < n:
    print(u, end=" ")
    u = u + r
    n_ = n_ + 1