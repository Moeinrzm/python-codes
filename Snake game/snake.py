import turtle
import time
starting = [(0, 0), (-20, 0), (-40, 0)]
class snake:
    def __init__(self):
        self.parts=[]
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for i in starting:
            self.add_part(i)


    def add_part(self, position):
        part = turtle.Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.parts.append(part)
    def extend(self):
        self.add_part(self.parts[-1].position())    

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[i - 1].xcor()
            new_y = self.parts[i- 1].ycor()
            self.parts[i].goto(new_x, new_y)
        self.head.forward(20) 
    
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
















