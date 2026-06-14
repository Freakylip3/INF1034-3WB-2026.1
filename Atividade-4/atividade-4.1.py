from turtle import *
from time import sleep 

t = Turtle()
t.speed(0)

def raiz(x):
    return x**0.5 

def divisao(x):
    return 1/x

def quadrado(x):
    return 2**x

def quartafuncao(X):
    return 5 - x**2

def quintafuncao(x):
    return x**2 - 5*x + 6

def sextafuncao(x):
    return x**3 - x**2 - x +1 

#Plano cartesiano

def plano_cartesiano(X, Y, TAMANHO, x, y, tamanho):
    t.pu()
    t.goto(X, Y)
    t.pd()
    t.lt(90)
    t.fd(TAMANHO)
    t.stamp()
    t.pu()
    t.goto(x, y)
    t.pd()
    t.rt(90)
    t.fd(tamanho)
    t.stamp()


t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)



t.color('red')
t.pu()
t.goto(0, 0)
t.pd()
for x in range(1, 201):
    t.goto(x*2, raiz(x*2))
sleep(2)
t.clear()

#função 1/x

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)

t.color('purple')
#esq
t.pu()
x= -300
y= divisao(x/50) * 10
t.goto(x, y)
t.pd()
for x in range(-299, 0 ):
    y = divisao(x/50) * 10
    t.goto(x, y)

#dir
t.pu()
x= 1
y= divisao(x/50) *10
t.goto(x,y)
t.pd()
for x in range(2, 301):
    y= divisao(x/50) * 10
    t.goto(x,y)
sleep(2)
t.clear()



#função 2^x

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)


t.color('pink')
t.pu()
x= -100
y= quadrado(x) 
t.goto(x * 3, quadrado(x))
t.pd()
for x in range (-75, 200):
    y= quadrado(x)
    t.goto(x*3 , y)

sleep(2)
t.clear()

#quarta funcao

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)

t.color('cyan')
t.pu()
x= -100
y= quartafuncao(x)
t.goto(x,y)
t.pd()
for x in range (-100, 101):
    y = quartafuncao(x)
    t.goto(x*3,y*3)
sleep(2)
t.clear()

#quinta funcao

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)

t.color('yellow')
t.pu()
x=-100
y= quintafuncao(x)
t.goto(x,y)
t.pd()
for x in range(-100, 101):
    y=quintafuncao(x)
    t.goto(x*3,y*3)
sleep(2)
t.clear()

#sexta funcao

t.color('black')
plano_cartesiano(0, -500, 900, -500, 0, 970)

t.color('green')
t.pu()
x= -100
y= sextafuncao(x)
t.goto(x,y)
t.pd()
for x in range(-100, 101):
    y= sextafuncao(x)
    t.goto(x*3,y*3)
sleep(2)
t.clear()

mainloop()