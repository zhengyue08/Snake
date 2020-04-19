from turtle import *
import threading
unit = 20
snake = Turtle()
screen = Screen()
snake_list = [(0,0),(0,unit),(0,unit*2),(0,unit*3),(0,unit*4),(0,unit*5)]
snake_dir="up"

def drawSnake(snake_list):
    snake.hideturtle()
    tracer(0)
    snake.shape("square")
    snake.pencolor("red")
    for i in snake_list:
        if i==snake_list[-1]:
            snake.penup()
            snake.fillcolor("red")
            snake.goto(i)
            snake.stamp()

        else:
            snake.penup()
            snake.fillcolor("black")
            snake.goto(i)
            snake.stamp()




def goUp():
    global snake_dir
    snake_dir = "up"
def goRight():
    global snake_dir
    snake_dir = "right"


def goDown():
    global snake_dir
    snake_dir = "down"

def goLeft():
    global snake_dir
    snake_dir = "left"
def control():
    screen.listen()
    screen.onkey(goLeft,"Left")
    screen.onkey(goRight, "Right")
    screen.onkey(goUp, "Up")
    screen.onkey(goDown, "Down")


def mainMove():
    snake.clearstamps()
    del snake_list[0]
    control()
    if snake_dir=="right":
        snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
    if snake_dir=="left":
        snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
    if snake_dir=="up":
        snake_list.append((snake_list[-1][0] , snake_list[-1][1]+unit))
    if snake_dir=="down":
        snake_list.append((snake_list[-1][0] , snake_list[-1][1]-unit))
    drawSnake(snake_list)
    screen.ontimer(mainMove,200)


def a():
    thread=threading.Thread(target=mainMove)
    thread.start()
a()
done()