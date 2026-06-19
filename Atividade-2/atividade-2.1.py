from turtle import *


t = Turtle()
t.speed(8)
#plano cartesiano

t.pu()
t.goto(0, -500)
t.pd()
t.lt(90)
t.fd(900)
t.stamp()
t.pu()
t.goto(-500, 0)
t.pd()
t.rt(90)
t.fd(950)
t.stamp()


#1

t.pu()
t.goto(200, 200)
t.pd()
color = textinput('Obter cor', 'Digite a cor')
t.color(color)
t.begin_fill()
for _  in range(12):
    t.fd(40)
    t.lt(30)
t.end_fill()
    

#2

t.pu()
t.goto(-200, 200)
t.pd()
color = textinput('Obter cor', 'Digite a cor')
t.color(color)
t.begin_fill()
for _ in range (6):
    t.fd(80)
    t.lt (60)
t.end_fill()


#3

t.pu()
t.goto(200,-200)
t.pd()
color = textinput('Obter cor', 'Digite a cor')
t.color(color)
t.begin_fill()
for _ in range (3):
    t.fd(100)
    t.lt(120)
t.end_fill()


#4

t.pu()
t.goto(-200,-200)
t.pd()
color = textinput('Obter cor', 'Digite a cor')
t.color(color)
t.begin_fill()
for _ in range (10):
    t.fd(60)
    t.lt(40)
t.end_fill()

# espiral

t.pu()
t.goto(-300, -300)
t.pd()
for i  in range(40):
    t.fd(i*1.10)
    t.lt(30)


mainloop()
