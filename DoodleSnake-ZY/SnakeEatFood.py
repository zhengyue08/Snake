from turtle import *
import threading
import random
unit = 20
snake = Turtle();snake.hideturtle()
food = Turtle()
food.hideturtle()
food.shape("square")
food.fillcolor("white")
food.turtlesize(1.5)
food.penup()
screen = Screen()
screen.setup(500,500)
snake_list = [(0,0),(0,unit),(0,unit*2),(0,unit*3),(0,unit*4),(0,unit*5)]
stamp_list = []
food_dic = {}
snake_dir="up"
foodsize=0
foodnumber=9

def creatFood():
    global food_dic
    tracer(0)
    food.hideturtle()
    for i in range(1, 10):
        food.penup()
        foodxy = (random.randrange(-220, 240,40), random.randrange(-220, 240, 40))
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
        # disx = head[0] - foodxy[0]
        # disy = head[1] - foodxy[1]
        if (disx==0) and (disy==0):
            foodsize=food_dic[foodxy]
            del food_dic[foodxy]
            food.pencolor("white")
            food.goto(foodxy)
            food.stamp()
            return True
    return False

def move():
    global foodnumber
    global foodsize
    global add
    global isfoodN
    # drawSnake(snake_list)
    snake.clearstamps()
    deci=isEaten()
    if deci==True:
        foodnumber-=1
        print(foodnumber)
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
    if foodnumber==0:
        food.goto((0,0))
        food.pencolor("orange")
        food.write("You are the WINNER",align="center",font=["Optima Bold",50])
    screen.ontimer(move,200)




creatFood()
print(food_dic)
move()

done()