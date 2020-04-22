# Snake
![截屏2020-04-22 下午12.21.23.png](https://i.loli.net/2020/04/22/1Tvsnmj63NRtWMF.png)
_(Snake.py is the formal source file of the game)_
## Design
+ We can divide the game into two parts - 
**game start interface**-`startUI()` and the **body of the game**. 
Only one thing need to be deal with - 
the original position of monster. I connect them using a variabal `monPosition`set on the top of the code, so when we use it in the `startUI()`and `monsterMove()`for the first time, it's same.
+ I create three objects (snake, monster,foods) using`Turtle()` and set there original 
features by initializing parameters of `pen()`and`shape()`on the top of codes. I describe how I achieve their movement in my work following.
  - **Snake**
    - **In our screen the only regular thing is the coordinate. So I define a list`snake_list`to record the coordinates of snake.Change it as we want and then we can achieve most of the function of snake.**
    - **Create a static snake**.  
    According to the assignment documents, we should use `turtle.stamp()` to create the Snake. By refering https://docs.python.org/3/library/turtle.html and trying for some simple examples, I know that `turtle.stamp()`works just like a **stamp**. We can change the **shape**, the **pencolor**, the **fillcolor**, and we move it to a **given position** and use `turtle.stamp()`, we can get a stamp we want, so I creat the funtion `drawSnake()` to create stamps according to the coordinates in `snake_list`
    
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
      ```
      
    -  **Change the `snake_list` as we want**.  
    I define the function `snakeMain()` to achieve the **movement** of snake based on `snake_list` and `ontimer()`.Just to append the coordinate we want to the `snake_list`, and delet the `snake_list[-1]` we can achieve teh movement. `ontimer()` will invoke `snakeMain()` after a regular time we set. so the snake moves continuously.   
    To **control the direction**. I define a variable `snake_dir` to **record the direction** we choose. `snakeMain()`will append the coordinate according to `snake_dir`.
        ```python
        if snake_dir == "right" :
            if (head[0]<230):
                snake_list.append((snake_list[-1][0] + unit, snake_list[-1][1]))
            else:
                snake_list.insert(0,tail)
        if snake_dir == "left" :
            if (-230<head[0]):
                snake_list.append((snake_list[-1][0] - unit, snake_list[-1][1]))
            else:
                snake_list.insert(0,tail)
        if snake_dir == "up" :
            if (head[1]<230):
                snake_list.append((snake_list[-1][0] , snake_list[-1][1] +unit))
            else:
                snake_list.insert(0,tail)
        if snake_dir == "down":
            if (-230<head[1]):
                snake_list.append((snake_list[-1][0], snake_list[-1][1] - unit))
            else:
                snake_list.insert(0,tail)
        ```
    In the codes below we add some conditions to avoid the snake move out of screen.
   - **Monster**  
   Different from snake, monster is only one square. So we just use the turtle's head as the monster.To chase the snake, we need to compare the coordinates of head of snake and monster,and invoke `turtle.goto()` to move it. For the velocity of Monster, I create a linear function to 
change.
      ```python
      def vMonster(head,monPosition):
          dis=(((head[0]-monPosition[0])//20)**2+((head[1]-monPosition[1])//20)**2)**0.5
          vMon=int(dis+5)*3
          return vMon
          ```
  - **Food**  
    -Create **Food** is not a problem, but how to make the snake extend while eating a food is the problem. In my work, I define a variable called `foodsize` ,if `foodsize>0`, it refers that snake need to extend - don't delet the `snake[-1]` in function`snakeMain()`.
    
      
