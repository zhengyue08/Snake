from turtle import *
import random

tracer(0)
snake = Turtle()
monster = Turtle()
screen = Screen()
screen.setup(500,500)

monster.shape("square")
monster.penup()
monster.goto(random.randrange(-200,200,20),random.randrange(-200,200,20))
monster.pendown()
monster.fillcolor("purple")
food = Turtle()
food.hideturtle()
for i in range(1,10):
    food.penup()
    food.goto(random.randrange(-200,200,20),random.randrange(-200,200,20))
    food.pendown()
    food.write(i,font=["Arial Bold", 20])



done()