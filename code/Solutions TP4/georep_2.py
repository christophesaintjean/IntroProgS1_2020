from turtle import *

n = int(input("Nombre de cotés ? "))

for i in range(n):
    forward(80)
    left(360/n)

exitonclick()
