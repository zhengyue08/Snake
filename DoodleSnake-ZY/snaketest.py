from turtle import *
snake = Turtle()
snake_list = [(0,100),(20,100),(40,100),(60,100),(80,100)]
stamp_list = []
def drawSnake(snake_list):
    snake.hideturtle()
    tracer(0)
    snake.penup()
    snake.goto(snake_list[0])
    snake.shape("square")
    snake.pencolor("red")
    snake.pendown()
    for i in snake_list:
        if i==snake_list[-1]:
            snake.penup()
            snake.fillcolor("red")
            snake.goto(i)
            snake.pendown()
            # snake.stamp()
            a=snake.stamp()
            stamp_list.append(a)
        else:
            snake.penup()
            snake.goto(i)
            snake.pendown()
            # snake.stamp()
            a = snake.stamp()
            stamp_list.append(a)
    update()
drawSnake(snake_list)

done()
