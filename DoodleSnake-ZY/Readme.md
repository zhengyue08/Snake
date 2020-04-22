# Snake
_(Snake.py is the formal source file of the game)_
## Design
+ We can divide the game into two parts - 
**game start interface**-`startUI()` and the **body of the game**. 
Only one thing need to be deal with - 
the original position of monster. I connect them using a variabal `monPosition`set on the top of the code, so when we use it in the `startUI()`and `monsterMove()`for the first time, it's same.
+ I create three objects (snake, monster,foods) using`Turtle()` and set there original 
features by initializing parameters of `pen()`and`shape()`on the top of codes. I describe how I achieve their movement in my work.
  - **Snake**
    - **In our screen the only regular thing is the coordinate. So I define a list`snake_list`to record the coordinates of snake.Change it as we want
    - First, we should create a static snake. According to the assignment documents, we should use `turtle.stamp()` to create the Snake. By refering https://docs.python.org/3/library/turtle.html and trying for some simple examples, I know that `turtle.stamp()`works just like a **stamp**. We can change the **shape**, the **pencolor**, the **fillcolor**, and we move it to a position using `turtle.stamp()`, we can get a stamp we want, so I creat the funtion `drawSnake()` to create stamps we want according to  `snake_list`
      ```python
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
    - Second, we just need to change the `snake`
