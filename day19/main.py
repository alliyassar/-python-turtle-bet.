from turtle import Turtle,Screen

tim= Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)
screen.listen()


def right():
    tim.right(10)
def left():
    tim.left(10)
def forward_ ():
    tim.forward(10)
def back_ward():
    tim.forward(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.down()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="w", fun=forward_)
screen.onkey(key="a",fun=left)
screen.onkey(key="s",fun=back_ward)
screen.onkey(key="d",fun=right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()
