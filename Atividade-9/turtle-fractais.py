from turtle import *
from random import randint
from time import sleep
t=Turtle()

t.speed(6)
t.clear
t.speed(0)
colormode(255)
t.clear


def randomColor():
    r= randint(40, 255)
    g= randint(40, 255)
    b= randint(40, 255)
    return (r, g, b)


def drawSquare(t, size):
  # t.goto(x, y)
    t.pu()
    t.begin_fill()
    t.fillcolor(randomColor())
    for i in range(4):
        t.fd(size)
        t.right(90)
    t.end_fill()
    t.pu()


def drawSquareFractal(t, size, step=50):
    if step < 0 or size < 1:
        return
    t.pd()
    t.fd(size / 1.5)
    t.lt(10)
    drawSquare(t, size)
    drawSquareFractal(t, size - 0.5, step - 0.4)


def drawSpiral(t):
  for i in range(250):
    t.fd(i)
    t.lt(15)


def drawStarFractal(t, size):
    if size < 10:
        return
    for i in range(6):
        t.begin_fill()
        t.color(randomColor())
        t.fd(size)
        drawStarFractal(t, size / 3)
    t.lt(216)
    t.stamp()
    t.end_fill()


def tree(t, size):
    if size == 0:
        return
    t.color(randomColor())
    t.fd(size)
    t.lt(30)
    tree(t,size-10)
    t.rt(60)
    tree(t,size-10)
    t.lt(30)
    t.bk(size)
    t.stamp()

def triforce(t, size):
    t.color("yellow")
    if size < 20:
        return
    for _ in range(3):
        triforce(t, size/2)
        t.fd(size)
        t.lt(120)

def treeFractal(t, size, angle, nivel):
  if size < 40:
    return
  t.pd()
  t.fd(size)

  # right tree
  t.rt(angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)

  t.color(randomColor())

  # left tree
  t.lt(2 * angle)
  t.fd(size)
  treeFractal(t, size * 0.8, angle, nivel - 1)
  t.back(size)
  t.stamp()

  t.pencolor(randomColor() )
  t.lt(-angle)
  t.back(size)
  t.stamp()



t.screen.bgcolor("black")
t.goto(-100, -200)
t.pd()
drawSquareFractal(t, 70, 60)
sleep(2)
t.clear()
t.screen.bgcolor("black")
t.goto(-100, -100)
t.pd()
drawStarFractal(t, 200)
sleep(2)
t.pu()
t.clear()
t.goto(0, -200)
t.lt(90)
t.setheading(90)
t.pd()
tree(t, 90)
t.clear()
t.screen.bgcolor("green")
t.pu()
t.goto(-150, -100)
t.pd()
triforce(t, 300)
sleep(2)
t.clear()
t.pu()
t.goto(0, 50)
t.setheading(0)
t.pd()
t.screen.bgcolor("blue")
t.lt(90)
treeFractal(t, 80, 40, 20)
t.setheading(180)
treeFractal(t, 80, 30, 5)
t.setheading(270)
treeFractal(t, 80, 30, 5)
t.setheading(360)
treeFractal(t, 80, 30, 5)






mainloop()