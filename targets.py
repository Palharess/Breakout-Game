from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Targets(Turtle):
    def __init__(self):
        super().__init__()
        self.targets = []
    
    def create_targets(self):
        x = -345
        y = 220
        while y > 60:
            while x < 345:
                target = Turtle()
                target.shape("square")
                target.ht()
                target.penup()
                target.color(random.choice(COLORS))
                target.turtlesize(stretch_len=2.5, stretch_wid=1)
                target.setpos(x= x, y = y)
                target.st()
                self.targets.append(target)
                x += 53
            y -= 30
            x = -345