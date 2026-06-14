from turtle import *
from time import sleep
t = Turtle()
t.speed(0)

def retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for _ in range (2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()

def circulo(x, y, color, raio):
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(raio)
    t.end_fill()

def triangulo(x, y, lado, angulo, color):
    t.speed(5)
    t.pu()
    t.goto(x,y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    t.rt(angulo)
    t.fd(lado)
    t.rt(angulo*2)
    t.fd(lado)
    t.rt(angulo*3)
    t.fd(lado)
    t.setheading(0)
    t.end_fill()

def desenha_frança():
    retangulo(-300, 300, 150, 250, "#022551")
    retangulo(-150, 300, 150, 250,"white")
    retangulo(0, 300, 150, 250, "#C71126")
    sleep(2)
    t.clear()

def desenha_italia():
    retangulo(-300, 300, 150, 250, "green")
    retangulo(-150, 300, 150, 250,"white")
    retangulo(0, 300, 150, 250, "red")
    sleep(2)
    t.clear()


def desenha_holanda():
    retangulo(-300, 300, 600, 150, "#022551")
    retangulo(-300, 150, 600, 150,"white")
    retangulo(-300, 0, 600, 150, "#C71126")
    sleep(2)
    t.clear()

def desenha_russia():
    retangulo(-300, 300, 600, 150, "#C71126")
    retangulo(-300, 150, 600, 150,"white")
    retangulo(-300, 0, 600, 150, "#022551")
    sleep(2)
    t.clear()

def desenha_alemanha():
    retangulo(-300, 300, 600, 150, "#000000")
    retangulo(-300, 150, 600, 150,"#D60100")
    retangulo(-300, 0, 600, 150, "#F7C703")
    sleep(2)
    t.clear()

def desenha_gabao():
    retangulo(-300, 300, 600, 150, "#03995D")
    retangulo(-300, 150, 600, 150,"#F4CB16")
    retangulo(-300, 0, 600, 150, "#3971BE")
    sleep(2)
    t.clear()

def desenha_iemen():
    retangulo(-300, 300, 600, 150, "#C71126")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#000000")
    sleep(2)
    t.clear()
    
def desenha_austria():
    retangulo(-300, 300, 600, 150, "#C71126")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#C71126")
    sleep(2)
    t.clear()
    
def desenha_colombia():
    retangulo(-300, 300, 600, 200, "#F7C703")
    retangulo(-300, 100, 600, 100,"#002F83")
    retangulo(-300, 0, 600, 100, "#C2112C")
    sleep(2)
    t.clear()

def desenha_hungria():
    retangulo(-300, 300, 600, 150, "#C82837")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#466C4E")
    sleep(2)
    t.clear()

def desenha_polonia():
    retangulo(-300,150,600,225,"white")
    retangulo(-300,-75,600,225,"red" )
    sleep(2)
    t.clear()

def desenha_niger():
    retangulo(-300, 300, 600, 150, "#D84F06")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#0CAB2A")
    circulo(0, 25, "#D84F06", 50)
    sleep(2)
    t.clear()

def desenha_EmiArab():
    retangulo(-300, 300, 600, 150, "#01843E")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#000000")
    retangulo(-300, 300, 150, 450, "#C8112E")
    sleep(2)
    t.clear()

def desenha_Palestina():
    retangulo(-300, 300, 600, 150, "#01843E")
    retangulo(-300, 150, 600, 150,"#F7F7F7")
    retangulo(-300, 0, 600, 150, "#000000")
    triangulo(-300, 300, 319, 45, "#C8112E")
    sleep(2)
    t.clear()

def desenha_bahamas():
    retangulo(-300, 300, 600, 150, "#37a4de")
    retangulo(-300, 150, 600, 150,"yellow")
    retangulo(-300, 0, 600, 150, "#37a4de")
    triangulo(-300, 300, 319, 45, "black")
    sleep(2)
    t.clear()

def desenha_japao():
    retangulo(-300, 300, 600, 450, "white")
    circulo(0, -10, "red", 90)
    sleep(2)
    t.clear()

desenha_polonia()
desenha_italia()
desenha_japao()
desenha_bahamas()
desenha_Palestina()
desenha_EmiArab()
desenha_niger()
desenha_frança()
desenha_holanda()  
desenha_russia()
desenha_alemanha()
desenha_gabao()
desenha_iemen()
desenha_austria()
desenha_colombia()
desenha_hungria()


mainloop()
