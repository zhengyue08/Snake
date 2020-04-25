from turtle import *
import threading
import random
import time
import sys
unit = 20
screen = Screen()
screen.setup(500,500)
screen.title("Enjoy your Game")
tracer(0)

food = Turtle();food.hideturtle()
food.shape("square")
food.turtlesize(1.5)
food.pen(fillcolor="white",pendown="False")
food_dic = {}
foodsize=0
foodnumber=9

snake = Turtle();snake.hideturtle()
snake_list = [(0,0)]
direction_monster="up"
head =(0,0)
tail =(0,0)

monster = Turtle()
monster.penup()
monster.ht()
monster.shape("square")
monster.pencolor("purple")
monster.fillcolor("purple")
monPosition= (random.randrange(-230,230,10),random.randrange(-200,-50,10))
monster.goto(monPosition)

start=0
end=0


def startUI():
    global monPosition
    tracer(0)
    shape("square")
    hideturtle()
    penup()
    goto(-200,100)
    write("Welcome to Richard's version of Snake\n\n"
          "You are going to use the 4 arrow keys to move the snake\n"
          "around the screen, trying to consume all the food items\n"
          "before the monster catches you...\n\n"
          "click anywhere to start the game, have fun!!",font=["Arial Bold",15])
    goto(0,0)
    pen(pencolor="red",fillcolor="red")
    stamp()
    goto(monPosition)
    pen(pencolor="purple",fillcolor="purple")
    stamp()
    update()

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


def vMonster(head,monPosition):
    dis=(((head[0]-monPosition[0])//20)**2+((head[1]-monPosition[1])//20)**2)**0.5
    vMon=int(dis+5)*3
    return vMon

def goUp():
    global direction_monster
    if direction_monster == "right" or direction_monster == "left":
        direction_monster = "up"
def goRight():
    global direction_monster
    if direction_monster == "up" or direction_monster == "down":
        direction_monster = "right"
def goDown():
    global direction_monster
    if direction_monster=="right" or direction_monster=="left":
        direction_monster = "down"
def goLeft():
    global direction_monster
    if direction_monster=="up" or direction_monster=="down":
        direction_monster = "left"

def control():
    screen.listen()
    screen.onkey(goLeft,"Left")
    screen.onkey(goRight, "Right")
    screen.onkey(goUp, "Up")
    screen.onkey(goDown, "Down")
    screen.onkey(pasueGame, "space")

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
            foodnumber-=1
            del food_dic[foodxy]
            food.pencolor("white")
            food.goto(foodxy)
            food.stamp()
            return True
    return False

def monsterMove():
    if not mRun:
        return
    renewtitle()
    global monPosition
    monster.st()
    # monster.pendown()
    vMon=vMonster(head,monPosition)
    x=head[0]-monPosition[0]
    y=head[1]-monPosition[1]
    if x>0 and y>0:
        if abs(x)>abs(y):
            monster.goto(monPosition[0] + vMon, monPosition[1])
        else:
            monster.goto(monPosition[0], monPosition[1] + vMon)
    if x>0 and y<0:
        if abs(x)>abs(y):
            monster.goto(monPosition[0] + vMon, monPosition[1])
        else:
            monster.goto(monPosition[0], monPosition[1] - vMon)
    if x<0 and y>0:
        if abs(x)>abs(y):
            monster.goto(monPosition[0] - vMon, monPosition[1])
        else:
            monster.goto(monPosition[0], monPosition[1] + vMon)
    if x<0 and y<0:
        if abs(x)>abs(y):
            monster.goto(monPosition[0] - vMon, monPosition[1])
        else:
            monster.goto(monPosition[0], monPosition[1] - vMon)
    monPosition = monster.pos()
    screen.ontimer(monsterMove,500)

def snakeMain():
    if not sRun:
        return
    global head
    global foodsize
    global tail
    global monPosition
    global snake_list
    global start
    renewtitle()
    tail=snake_list[0]
    snake.clearstamps()
    isEaten()
    control()
    lenth=len(snake_list)
    controlSnakev = 200
    if lenth>5:
        if foodsize==0 :
            del snake_list[0]
            controlSnakev=200
        else:
            foodsize-=1
            controlSnakev =400
    if direction_monster == "right" :
        # snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
        if (head[0]<230):
            snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
        else:
            snake_list.insert(0,tail)
    if direction_monster == "left" :
        # snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
        if (-230<head[0]):
            snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
        else:
            snake_list.insert(0,tail)
    if direction_monster == "up" :
        # snake_list.append((snake_list[-1][0] , snake_list[-1][1]+unit))
        if (head[1]<230):
            snake_list.append((snake_list[-1][0] , snake_list[-1][1] +unit))
        else:
            snake_list.insert(0,tail)
    if direction_monster == "down":
        # snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
        if (-230<head[1]):
            snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
        else:
            snake_list.insert(0,tail)
    drawSnake(snake_list)
    gameExit(foodnumber,head,monPosition)
    screen.ontimer(snakeMain,controlSnakev)


def gameExit(foodnumber,head,monPosition):
    if foodnumber<=0:
        food.goto((0,0))
        food.pencolor("orange")
        food.write("You are the WINNER\n",align="center",font=["Optima Bold",50])
        food.write("Good", align="center", font=["Optima Bold", 25])
        time.sleep(8)
        sys.exit()
        # end=time.perf_counter()
    if abs(head[0]-monPosition[0])<=8 and abs(head[1]-monPosition[1])<=8:
        food.goto((0, 0))
        food.pencolor("red")
        food.write("Game Over!\n", align="center", font=["Optima Bold", 50])
        food.write("Try again", align="center", font=["Optima Bold", 25])
        time.sleep(8)
        sys.exit()
        # end = time.perf_counter()


def interesct():
    a = 1
    b = 0
    global track_keep
    track_keep_pre = track_keep
    track_keep = []
    x_m = monPosition[0] / 20
    y_m = monPosition[1] / 20
    counting = 1
    length = len(snake_list)
    while counting <= length:
        findL = counting - 1
        cor2 = snake_list[findL]
        print('snake'+str(cor2))
        xcor2 = cor2[0] / 20
        ycor2 = cor2[1] / 20
        delX = abs(xcor2 - x_m)
        print(delX)
        delY = abs(ycor2 - y_m)
        print(delY)
        counting = counting + 1
        if (delX <= 1) and (delY <= 1):
            track_keep.append(counting)
    if track_keep_pre == []:
        if track_keep != []:
            return a
        else:
            return b
    else:
        return b

def renewtitle():
    global termin
    global contacttime
    newtime = interesct()
    contacttime = contacttime + newtime
    termin = time.perf_counter()
    titletxt = "Time: " + str(int(termin - begin))+", Contact: " + str(contacttime)
    screen.title(titletxt)


def pasueGame():
    global sRun
    global mRun
    global pausewhen
    pausewhen = time.perf_counter()
    sRun = False
    mRun = False
    screen.onkey(continueGame, "space")
    screen.listen()
    done()


def continueGame():
    global mRun
    global sRun
    global begin
    resumwhen = time.perf_counter()
    correction = resumwhen - pausewhen
    begin = begin + correction
    sRun = True
    mRun = True
    ontimer(snakeMain, 100)
    ontimer(monsterMove, 100)
    return


startUI()


def main(x,y):
    global begin
    global contacttime
    global track_keep
    global mRun
    global sRun
    mRun = True
    sRun = True
    track_keep=[]
    contacttime=0
    begin=time.perf_counter()
    clear()
    creatFood()
    monsterMove()
    snakeMain()

screen.onclick(main)

done()
