from turtle import *
screen=Screen()
monster = Turtle()
monster.hideturtle()
monster.penup()
monster.shape("square")
monster.pencolor("purple")
monster.fillcolor("purple")
monPosition= (0,0)
snake_dir = "up"
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

def monsterMove():
    global snake_dir
    global monPosition
    id=monster.stamp()
    monster.clearstamp(id)
    control()
    if snake_dir=="up":
        monster.goto(monPosition[0] ,(monPosition[1]+40))
        # monster.stamp()
    if snake_dir=="down":
        monster.goto(monPosition[0] , (monPosition[1]-40))
       # monster.stamp()
    if snake_dir=="right":
        monster.goto((monPosition[0] + 40) , monPosition[1])
        # monster.stamp()
    if snake_dir=="left":
        monster.goto((monPosition[0] - 40) , monPosition[1])
        # monster.stamp()
    # monster.stamp()
    monPosition = monster.pos()
    # monster.stamp()
    screen.ontimer(monsterMove,250)


monsterMove()
done()

