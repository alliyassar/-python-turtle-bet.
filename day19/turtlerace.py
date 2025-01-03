from turtle import Turtle,Screen
import random

is_on=True
screen=Screen()
screen.bgpic("bg.gif")
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race ?Enter a color")
print(user_bet)
location = -150
turtle_colors=["red","green","blue","purple","yellow"]
all_turtles=[]

for each_turtle in range(0,5):
    new_turtles = Turtle()
    new_turtles.color(turtle_colors[each_turtle])
    new_turtles.shape("turtle")
    new_turtles.penup()
    new_turtles.goto(x=-240, y=location)
    all_turtles.append(new_turtles)
    location+=50

while is_on:
        for turtle in all_turtles:
            rand_distance=random.randint(0,10)
            turtle.forward(rand_distance)
            if turtle.xcor()>230:
                winner_color=turtle.pencolor()
                is_on=False
                winner=Turtle()
                winner.hideturtle()
                winner.penup()
                winner.goto(0, 0)
                winner.write(f"The winner is {winner_color}",align="center",font=("Arial",34,"bold"))



screen.exitonclick()