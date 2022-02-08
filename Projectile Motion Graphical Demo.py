from sqlite3 import SQLITE_CREATE_INDEX
from time import time
from tkinter import Grid
import turtle
world_x = 140
world_y = 140

#Computing Module of Projectile Motion
def y(s, u, a = -9.81):
    while s >= s:
        last_time = time()
        delta_t = float(time() - last_time, 2)
        #Assuming upward is positive
        return u*delta_t + 0.5*a*(delta_t**2)

#Setting Up The Turtle Window
def initialize_turtle():
    turtle.title("Projectile Motion Graphical Demostration")
    turtle.setworldcoordinates(0, 0, world_x, world_y)
    turtle.up()
    turtle.goto(0, 20)

def creating_xy_axis(): 
    turtle.speed(0)
    turtle.pensize(2)  
    turtle.goto(20, 20)
    turtle.down()
    turtle.goto(20, 120)
    turtle.setheading(90)
    turtle.stamp()
    turtle.write("y/unit")
    turtle.goto(20, 70)
    turtle.goto(120, 70)
    turtle.setheading(0)
    turtle.stamp()
    turtle.write("x/unit")

def drawing_grid(precision):
    grid = turtle.Turtle()
    grid.speed(0)
    grid.up()
    grid.home()
    grid.setheading(0)
    grid.pencolor("gray")
    for i in range(0, world_x, int(world_x/precision)):
        grid.goto(0,i)
        grid.down()
        grid.forward(world_x)
        grid.up()
    grid.setheading(90)
    for i in range(0, world_y, int(world_y/precision)):
        grid.goto(i,0)
        grid.down()
        grid.forward(world_y)
        grid.up()
    grid.hideturtle()


initialize_turtle()
drawing_grid(14)
creating_xy_axis()
turtle.done()