import turtle
from snake import snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen=turtle.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

Snake=snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(Snake.up, "Up")
screen.onkey(Snake.down, "Down")
screen.onkey(Snake.left, "Left")
screen.onkey(Snake.right, "Right")



check=True
while check:
    screen.update()
    time.sleep(0.1)
    Snake.move()
    
    if Snake.head.distance(food)<15:
        scoreboard.incresment()
        Snake.extend()
        food.refresh()

    if Snake.head.xcor()>290 or Snake.head.xcor()<-299 or Snake.head.ycor()<-290 or Snake.head.ycor()>299:
            check=False
            scoreboard.game_over()  
    for i in Snake.parts[1:]:
        if Snake.head.distance(i)<10:
            scoreboard.game_over()
            check=False
    

screen.exitonclick()