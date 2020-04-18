from turtle import *
import random

tracer(0)
snake = Turtle()
monster = Turtle()
screen = Screen()
screen.setup(500,500)

monster.shape("square")
monster.penup()
monster.goto(random.randint(-200,200),random.randint(-200,200))
monster.pendown()
monster.fillcolor("purple")
food = Turtle()
food.hideturtle()
for i in range(1,10):
    food.penup()
    food.goto(random.randint(-200,200),random.randint(-200,200))
    food.pendown()
    food.write(i,font=[10])



update()
done()