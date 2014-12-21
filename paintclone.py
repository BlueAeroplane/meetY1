import turtle
from turtle import *
turtle.speed(0)
turtle.hideturtle()
shape='circle'
z='black'
print("to change color to red press q")
print("to change color to yellow press w")
print("to change color to green press e")
print("to change color to black press r")
print("to change shape press s or c")
def circle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    begin_fill()
    fillcolor(z)
    turtle.circle(50)
    end_fill()
def square(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    begin_fill()
    fillcolor(z)
    turtle.goto(x+50,y)
    turtle.goto(x+50,y+50)
    turtle.goto(x,y+50)
    turtle.goto(x,y)
    end_fill()

def draw (x,y):
    global shape
    if shape=='circle':
        circle(x,y)
    elif shape=='square':
        square(x,y)

def choosec():
    global shape
    shape='circle'
    
def chooses():
    global shape
    shape='square'

def choosez():
    global z
    z='red'


def choosew():
    global z
    z='yellow'


def choosee():
    global z
    z='#00FF00'

def chooser():
    global z
    z='#000000'
    

turtle.getscreen().onkeypress(choosec,"c")
turtle.getscreen().onkeypress(chooses,"s")
turtle.getscreen().onkeypress(choosez,"q")
turtle.getscreen().onkeypress(choosew,"w")
turtle.getscreen().onkeypress(choosee,"e")
turtle.getscreen().onkeypress(chooser,"r")
turtle.onscreenclick(draw)
listen()
turtle.mainloop()
