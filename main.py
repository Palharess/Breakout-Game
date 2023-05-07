from turtle import *
from targets import Targets
import time, random
from ball import Ball

game_on = True
screen = Screen()
screen.setup(width=750, height=500)
screen.bgcolor("black")
screen.tracer(0)
t1 = Turtle("square")
t1.ht()
t1.color("blue")
t1.turtlesize(stretch_len=3.8, stretch_wid=0.7)
t1.penup()
t1.setposition(0,-220)
t1.st()

targets = Targets()
targets.create_targets()
screen.update()
screen.tracer(1)
ball = Ball()
ball.create_ball()
ball.start_angle()

def move():
    x = t1.xcor() + 40
    screen.onkeypress(t1.goto(x, t1.ycor()), "d")

def move_left():
    x = t1.xcor() - 40
    screen.onkeypress(t1.goto(x, t1.ycor()), "d")

screen.onkeypress(move, "d")
screen.listen()

while game_on:
    ball.check(t1=t1)
    screen.tracer(1)
    screen.onkeypress(move, "d")
    screen.onkeypress(move_left, "a")
    screen.listen()
    ball.move_ball(t1=t1, list=targets.targets)





screen.exitonclick()