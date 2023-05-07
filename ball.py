from turtle import*
import random

n = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.ball_object = []
        self.distance = 20
        self.direction_right = 0
        self.direction_left = 0
        self.speed = 1

    def create_ball(self):
        self.ball = Turtle()
        self.ball.shape("circle")
        self.ball.speed(self.speed)
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

    def move_ball(self,t1, list):
        global n
        n = 0
        self.ball.forward(self.distance)
        x, y = self.ball.position()

        self.screen.tracer(0)
        if self.ball.distance(t1.xcor(), t1.ycor()) <= 35:
            self.reflect_vertical()
            self.reflect_horizontal()
            self.screen.tracer(1)
            self.speed += 0.25
            self.ball.speed(self.speed)
            self.ball.forward(40)
            
        for item in list:
            if self.ball.distance(item.xcor(), item.ycor()) <= 35:
                item.clear()
                item.ht()
                self.reflect_vertical()
                self.screen.tracer(1)
                index = list.index(item)
                list.remove(list[index])
                break
        
    def reflect_horizontal(self):
        angle = self.ball.heading()
        self.ball.setheading(180 - angle)

    def reflect_vertical(self):
        global n
        if n == 0:
            angle = self.ball.heading()
            self.ball.setheading(-angle)
            n += 1

    def check(self, t1):
        if self.ball.ycor() < -223:
            print("f")
        elif self.ball.xcor() < -355 or self.ball.xcor() > 350:
            angle = self.ball.heading()
            reflect_angle = 180 - angle
            self.ball.setheading(reflect_angle)
            self.forward(40)
        elif self.ball.ycor() > 240:
            self.reflect_vertical()
