from turtle import*
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_object = []
        self.distance = 20
        self.direction_right = 0
        self.direction_left = 0

    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("turtle")
        self.ball.speed(1)
        self.ball.color("white")
        self.ball.penup()
        self.ball.turtlesize(stretch_len=0.7, stretch_wid=0.7)
        self.ball_object.append(self.ball)


    def start_angle(self):
        choice = random.randint(0,1)
        self.direction_right = random.randint(-270, -225)
        self.direction_left = random.randint(-90, -45)
        if choice == 0:
            self.ball.left(self.direction_left)
        else:
            self.ball.right(self.direction_right)

    def move_ball(self):
        self.ball.forward(self.distance)
    
    def check(self):
        if self.ball.ycor() < -223:
            print("f")
        elif self.ball.xcor() < -355 or self.ball.xcor() > 350:
            angle = self.ball.heading()
            reflect_angle = 180 - angle
            self.ball.setheading(reflect_angle)
