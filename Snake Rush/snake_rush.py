# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 00:50:51 2020

@author: asus
"""

import random
import turtle as t
from turtle import Screen
from playsound import playsound
screen= Screen()
screen.title("SNAKE RUSH")
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
snake_image=t.Turtle()
si="snakegif.gif"
si2="snakegif2.gif"
t.register_shape(si)
t.register_shape(si2)
t.penup()
text_start.penup()
t.setpos(0,-110)
text_start.setpos(0,-240)
snake_image.penup()
snake_image.setpos(0,120)
snake_image.shape(si)
snake_image.shapesize(1,1,1)
t.write("-♦♦SNAKE RUSH♦♦-",align="center",font=("Comic Sans MS",30,"bold"))
text_start.write("Press SPACE bar to start",align="center",font=("Courier",18,"bold"))
playsound("videoplayback.mp3",False )
text_start.hideturtle()
t.ht()
                 

text_score=t.Turtle()
text_score.hideturtle()
text_score.speed(0)


def displayScore(new_score):
    text_score.clear()
    text_score.penup()
    x= (t.window_width()/2)-50
    y= (t.window_height()/2)-60
    text_score.setpos(x,y)
    text_score.write(str(new_score),align="right",font=("Courier",40,"bold"))
    

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


def exitprogram():
    screen.bye()    

def gameOver():
    playsound("smb_mariodie.wav",False)
    t.bgcolor("yellow")
    snake.color("yellow")
    apple.color("yellow")
    t.penup()
    t.hideturtle()
    t.setpos(0,0)
    snake_image.shape(si2)
    snake_image.setpos(-20,130)
    snake_image.st()
    t.write("GAME OVER!", align="center", font=("Ariel",30,"normal"))
    text_score.clear()
    


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
    
    t.bgcolor("#00a720")
    score=0
    text_start.clear()
    snake_image.ht()
    t.clear()
    
    snake_speed=1    
    snake_length=3
    snake.shapesize(0.5,snake_length,0.5)
    snake.showturtle()
    displayScore(score)
    placeApple()
    
    while True:
        snake.forward(snake_speed)
        if snake.distance(apple)<27:
            playsound("button-3.wav",False )
            placeApple()
            snake_length+=1
            snake.shapesize(0.5,snake_length,0.5)
            snake_speed+=0.4
            score+=10
            displayScore(score)
        if outsideWindow():
            gameOver()
            t.setpos(0,-40)
            t.write("Score: "+str(score), align="center", font=("Courier",25,"bold"))
            text_start.write("Press ESC to exit", align="center", font=("Courier",25,"bold"))
            break
            

        
t.onkey(startGame, "space")
t.onkey(moveUp, "Up")
t.onkey(moveDown, "Down")
t.onkey(moveLeft, "Left")
t.onkey(moveRight, "Right")
t.onkey(exitprogram, "Escape")
t.listen()
t.mainloop()



screen.exitonclick()
