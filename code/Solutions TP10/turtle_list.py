import turtle as T

def rect(l, h, x=0, y=0):
    T.penup()
    T.setposition(x, y)
    T.pendown()
    T.forward(l)
    T.left(90)
    T.forward(h)
    T.left(90)
    T.forward(l)
    T.left(90)
    T.forward(h)
    T.left(90)

l = 30
h0 = 40
h1 = 100
h2 = 80
x0, y0 = -100, -100

rect(l, h0, x0+0*l, y0)
rect(l, h1, x0+1*l, y0)
rect(l, h2, x0+2*l, y0)

def histo(H, l, x, y):
    for i, hi in enumerate(H):
        rect(l, hi, x+ i * l, y)
        
def histo_2(H, l, x, y):
    for i in range(len(H)):
        rect(l, H[i], x+ i * l, y)
        
H = [100, 50, 120, 12, -30, 60, 250, 100]
        
T.clear()
histo(H, 30, -200, -200)
T.exitonclick()
        
    




T.exitonclick()
    
    
    