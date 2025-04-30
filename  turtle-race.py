import turtle
import random
colors=["red","black","orange","purple","yellow","blue"]
turtle1=turtle.Turtle()
screen=turtle.Screen()
screen.setup(width=500,height=400)
user=screen.textinput(title="choose your bet",prompt="which turtle will win the race? Enter a color:")
y=-150
all_turtles=[]
for i in range(6):
    new_turtle=turtle.Turtle()
    new_turtle.penup()
    new_turtle.shapesize(3)
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(-230,y)
    y+=60
    all_turtles.append(new_turtle)
x=''
race=True if user else False
while (race):
    for i in all_turtles:
        random_distance=random.randint(0,10)
        i.forward(random_distance)
        if i.xcor()>220:
            x=i.pencolor()
            if x==user:
                print(f"you won by choosing {x}")
            else:
                print (f"you lost,,,, the winner is {x}")
            race=False
        
screen.exitonclick()