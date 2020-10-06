from turtle import *

vitesse = int(input("Vitesse ? "))
speed(vitesse)

long = input("Longueur du coté ? (default: 100)")
if long:
    long = int(long)
else:
    long = 100

sens = input("Sens horaire ? ")
sens = bool(sens)
    

#################################

forward(long)

if sens:
    right(120)
else:
    left(120)

forward(long)

if sens:
    right(120)
else:
    left(120)

forward(long)

exitonclick()
