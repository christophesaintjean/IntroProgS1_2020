from turtle import *
import math

k = int(input("k ? "))

m = None
for i in range(179, 90, -1):
    if k*360 % i == 0:
        m = i
        break
        
if m == None:
    print("Pas de valeur trouvée")
else:
    print(m)

print(xcor(), ycor())
while True:
    forward(100)
    right(m)
    print(xcor(), ycor())
    if (math.isclose(xcor(), 0., abs_tol=1e-8) and
        math.isclose(ycor(), 0., abs_tol=1e-8)):
        break
exitonclick()