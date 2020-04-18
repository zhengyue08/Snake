from turtle import *
import random
bbb
def startUI():
    setup(width=500, height=500)
    hideturtle()
    penup()
    goto(-200,100)
    write("Welcome to Richard's version of Snake\n\n"
          "You are going to use the 4 arrow keys to move the snake\n"
          "around the screen, trying to consume all the food items\n"
          "before the monster catches you...\n\n"
          "click anywhere to start the game, have fun!!",font=["Arial Bold",15])
    done()

startUI()
