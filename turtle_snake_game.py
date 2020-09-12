# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:50:51 2020

@author: asus
"""

import random
import turtle as t
from turtle import Screen
screen= Screen()
t.bgcolor("yellow")


snake = t.Turtle()
snake.shape("square")
snake.color("black")
snake.speed(0)
snake.penup()
snake.hideturtle()


apple = t.Turtle()
apple.shape("circle")
apple.color("red")
apple.penup()
apple.hideturtle()
apple.speed(0)

game_started=False
text_start=t.Turtle()
text_start.write("Press SPACE bar to start",align="center",font=("Ariel",18,"bold"))
text_start.hideturtle()
                 

text_score=t.Turtle()
text_score.hideturtle()
text_score.speed(0)


def displayScore(new_score):
    text_score.clear()
    text_score.penup()
    x= (t.window_width()/2)-50
    y= (t.window_height()/2)-60
    text_score.setpos(x,y)
    text_score.write(str(new_score),align="right",font=("Ariel",40,"bold"))
    

def placeApple():
    apple.hideturtle()
    apple.setx(random.randint(-200, 200))
    apple.sety(random.randint(-200, 200))
    apple.showturtle()

def outsideWindow():
    left_boundary= -t.window_width()/2
    right_boundary= t.window_width()/2
    top_boundary= t.window_height()/2
    bottom_boundary= -t.window_height()/2
    (x,y)=snake.pos()
    outside= \
        x<left_boundary or \
            x>right_boundary or \
                y<bottom_boundary or \
                    y>top_boundary
    return outside
    

def gameOver():
    snake.color("yellow")
    apple.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("GAME OVER!", align="center", font=("Ariel",30,"normal"))


def moveUp():
    if snake.heading()==0 or snake.heading()==180:
        snake.setheading(90)
        
    
def moveDown():
    if snake.heading()==0 or snake.heading()==180:
        snake.setheading(270)
        
    
def moveLeft():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(180)
        
    
def moveRight():
    if snake.heading()==90 or snake.heading()==270:
        snake.setheading(0)
        

def startGame():
    global game_started
    if game_started:
        return
    game_started=True
    
    score=0
    text_start.clear()
    
    snake_speed=1    
    snake_length=3
    snake.shapesize(1,snake_length,1)
    snake.showturtle()
    displayScore(score)
    placeApple()
    
    while True:
        snake.forward(snake_speed)
        if snake.distance(apple)<20:
            placeApple()
            snake_length+=1
            snake.shapesize(1,snake_length,1)
            snake_speed+=0.4
            score+=10
            displayScore(score)
        if outsideWindow():
            gameOver()
            break

        
t.onkey(startGame, "space")
t.onkey(moveUp, "Up")
t.onkey(moveDown, "Down")
t.onkey(moveLeft, "Left")
t.onkey(moveRight, "Right")
t.listen()
t.mainloop()



screen.exitonclick()
