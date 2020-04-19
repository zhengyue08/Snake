from turtle import *
import threading
import random
unit = 20
snake = Turtle()
snake.hideturtle()
snake.shape("square")
snake.pencolor("red")
food = Turtle()
food.hideturtle()
food.shape("square")
food.fillcolor("white")
food.turtlesize(1.5)
food.penup()
screen = Screen()
screen.setup(500,500)
snake_list = [(10,-10),(10,unit-10),(10,unit*2-10),(10,unit*3-10),(10,unit*4-10),(10,unit*5-10)]
stamp_list = []
food_dic = {}
snake_dir="up"
foodsize=0
foodnumber=9
gamestatus="unstarted"
def gameStatus():
    global gamestatus
    gamestatus="started"
    print(gamestatus)

def startUI():
    hideturtle()
    penup()
    goto(-200,100)
    write("Welcome to Richard's version of Snake\n\n"
          "You are going to use the 4 arrow keys to move the snake\n"
          "around the screen, trying to consume all the food items\n"
          "before the monster catches you...\n\n"
          "click anywhere to start the game, have fun!!",font=["Arial Bold",15])
    snake.goto(0,0)
    snake.fillcolor("red")
    snake.stamp()


# startUI()
# done()

def creatFood():
    global food_dic
    tracer(0)
    food.hideturtle()
    for i in range(1, 10):
        food.penup()
        foodxy = (random.randrange(-220, 240,20), random.randrange(-220, 240, 20))
        food.goto(foodxy)
        # food.pendown()
        food.write(i,align="center",font=["Arial Bold",12])
        food_dic[foodxy]=i

def drawSnake(snake_list):
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
    update()

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
#方向总控
def control():
    screen.listen()
    screen.onkey(goLeft,"Left")
    screen.onkey(goRight, "Right")
    screen.onkey(goUp, "Up")
    screen.onkey(goDown, "Down")

def isEaten():
    global foodnumber
    global foodsize
    head= snake_list[-1]
    for foodxy in list(food_dic.keys()):
        disx=abs(head[0]-foodxy[0])
        disy=abs(head[1]-foodxy[1])
        if (disx<=10) and (disy<=10):
            foodsize=food_dic[foodxy]
            foodnumber-=1
            food.pencolor("white")
            food.goto(foodxy)
            food.stamp()
            return True
    return False

def moveMainofSnake():
    global foodsize
    global add
    # drawSnake(snake_list)
    snake.clearstamps()
    isEaten()
    if foodsize==0:
        del snake_list[0]
    else:
        foodsize-=1
    control()
    if snake_dir == "right":
        snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
    if snake_dir == "left":
        snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
    if snake_dir == "up":
        snake_list.append((snake_list[-1][0], snake_list[-1][1] + unit))
    if snake_dir == "down":
        snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
    drawSnake(snake_list)
    screen.ontimer(moveMainofSnake,200)

# def gameflow():
#     global gamestatus
#     screen.listen()
#     screen.onkey(clearscreen,"space")
#     startUI()
#     screen.onkey(moveMainofSnake, "space")
#     done()
# gameflow()