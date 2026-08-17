from turtle import *
from random import randint
from time import sleep
import tkinter as tk

root = tk.Tk()
slider = tk.Scale(root, from_=10, to=180, orient="horizontal", label="Ajustar Parâmetro")
slider.set(30)
slider.pack(padx=20, pady=10, fill="x")
t=Turtle()
tkinter = tk

t.speed(0)
colormode(255)
t.clear()


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

def atualizador(): ########################################################################################################################################################
    t.clear()
    t.clearstamps()
    t.pu(); t.goto(0, 0); t.setheading(90)
    valor_atual = slider.get() 
    
    t.goto(0, 0); t.setheading(270)
    treeFractal(t, size=80, angle=valor_atual, nivel=5)
    sleep(3)
    t.clear()
    drawSquareFractal(t,  valor_atual, 60)
    sleep(3)
    t.clear()
    t.pu()
    t.clear()
    t.goto(0, -200)
    t.lt(90)
    t.setheading(90)
    t.pd()
    tree(t, valor_atual)
    t.pd()
    tree(t, valor_atual)
    t.clear()
    t.screen.bgcolor("green")
    t.pu()
    t.pu()
    t.goto(-150, -100)
    t.pd()
    triforce(t, valor_atual)
    sleep(2)
    t.clear()
    t.pu()
    t.goto(0, 50)
    t.setheading(0)
    t.pd()
    t.screen.bgcolor("blue")
    t.lt(90)
    treeFractal(t, 80, valor_atual, 20)
    t.setheading(180)
    treeFractal(t, 80, valor_atual, 5)
    t.setheading(270)
    treeFractal(t, 80, valor_atual, 5)
    t.setheading(360)
    treeFractal(t, 80, valor_atual, 5)



botao = tk.Button(root, text="Atualizar Desenho", command=atualizador)
botao.pack(padx=20, pady=10, fill="x")

atualizador()

mainloop()