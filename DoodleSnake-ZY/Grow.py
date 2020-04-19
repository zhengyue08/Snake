from turtle import *
import threading
unit = 20
snake = Turtle()
snake.penup()
screen = Screen()
snake_list = [(10,0)]
snake_dir="up"
def growth():

def drawSnake(snake_list):
    tracer(0)
    snake.shape("square")
    snake.pencolor("red")
    for i in snake_list:
        if i == snake_list[-1]:
            snake.penup()
            snake.fillcolor("red")
            snake.goto(i)
            snake.stamp()
        else:
            snake.penup()
            snake.fillcolor("black")
            snake.goto(i)
            snake.stamp()
drawSnake(snake_list)
done()