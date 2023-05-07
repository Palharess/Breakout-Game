from turtle import*
import random

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.players = []

    def create_player(self):
        t1 = Turtle("square")
        self.players.append(t1)
        t1.ht()
        t1.color("blue")
        t1.turtlesize(stretch_len=3.8, stretch_wid=0.7)
        t1.penup()
        t1.setposition(0,-220)
        t1.st()