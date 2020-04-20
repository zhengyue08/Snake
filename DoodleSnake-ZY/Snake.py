from turtle import *
import threading
import random
import time
import sys
unit = 20
snake = Turtle();snake.hideturtle()
food = Turtle();food.hideturtle()

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
head =(0,0)
tail =(0,0)
monster = Turtle()
monster.ht()
monster.penup()
monster.shape("square")
monster.pencolor("purple")
monster.fillcolor("purple")
monPosition= (-120,-120)
tracer(0)
monster.goto(monPosition)



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
    if snake_dir == "right" or snake_dir == "left":
        snake_dir = "up"
def goRight():
    global snake_dir
    if snake_dir == "up" or snake_dir == "down":
        snake_dir = "right"
def goDown():
    global snake_dir
    if snake_dir=="right" or snake_dir=="left":
        snake_dir = "down"
def goLeft():
    global snake_dir
    if snake_dir=="up" or snake_dir=="down":
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
    global head
    head= snake_list[-1]
    for foodxy in list(food_dic.keys()):
        disx=abs(head[0]-foodxy[0])
        disy=abs(head[1]-foodxy[1])
        # disx = head[0] - foodxy[0]
        # disy = head[1] - foodxy[1]
        if (disx==0) and (disy==0):
            foodsize=food_dic[foodxy]+foodsize
            del food_dic[foodxy]
            food.pencolor("white")
            food.goto(foodxy)
            food.stamp()
            return True
    return False

def gameMain():
    global head
    global foodnumber
    global foodsize
    global tail
    global monPosition
    tail=snake_list[0]
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
    if snake_dir == "right" :
        # snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
        if (head[0]<230):
            snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
        else:
            snake_list.insert(0,tail)

    if snake_dir == "left":
        # snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
        if (-230<head[0]):
            snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
        else:
            snake_list.insert(0,tail)
    if snake_dir == "up":
        # snake_list.append((snake_list[-1][0] , snake_list[-1][1]+unit))
        if (head[1]<230):
            snake_list.append((snake_list[-1][0] , snake_list[-1][1] +unit))
        else:
            snake_list.insert(0,tail)
    if snake_dir == "down":
        # snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
        if (-230<head[1]):
            snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
        else:
            snake_list.insert(0,tail)
    drawSnake(snake_list)
    gameExit(foodnumber,head,monPosition)
    screen.ontimer(gameMain,200)
def monsterMove():
    global snake_dir
    global monPosition
    monster.st()
    control()
    # vMon=vMonster(head,monPosition)
    vMon = vMonster()
    if snake_dir=="up":
        if monPosition[1]<220:
            monster.goto(monPosition[0] ,(monPosition[1]+vMon))
    if snake_dir=="down":
        if monPosition[1]>(-230):
            monster.goto(monPosition[0] , (monPosition[1]-vMon))
    if snake_dir=="right":
        if monPosition[0]<230:
            monster.goto((monPosition[0] + vMon) , monPosition[1])
    if snake_dir=="left":
        if monPosition[0]>(-230):
            monster.goto((monPosition[0] - vMon) , monPosition[1])
    monPosition = monster.pos()
    screen.ontimer(monsterMove,400)

def gameExit(foodnumber,head,monPosition):
    if foodnumber<=0:
        food.goto((0,0))
        food.pencolor("orange")
        food.write("You are the WINNER\n",align="center",font=["Optima Bold",50])
        food.write("👍👍👍👍", align="center", font=["Optima Bold", 25])
        time.sleep(10)
        sys.exit()
    if abs(head[0]-monPosition[0])<=5 and abs(head[1]-monPosition[1])<=5:
        food.goto((0, 0))
        food.pencolor("red")
        food.write("Game Over!\n", align="center", font=["Optima Bold", 50])
        food.write("😂😂😂😂", align="center", font=["Optima Bold", 25])
        time.sleep(10)
        sys.exit()
# tracer(0)
# def vMonster(head, monPosition):
#     dis=(((head[0]-monPosition[0])//20)**2+((head[1]-monPosition[1])//20)**2)**1/2
#     vMon=3**dis*20
#     return vMon
def vMonster():
    global head
    global monPosition
    dis=(((head[0]-monPosition[0])//20)**2+((head[1]-monPosition[1])//20)**2)**0.5
    vMon=int(dis**2)
    print(vMon)
    return vMon
creatFood()
monsterMove()
gameMain()


# thread_snake=threading.Thread(target=snakeMove)
# thread_monster=threading.Thread(target=monsterMove)
# thread_snake.start()
# thread_monster.start()
done()