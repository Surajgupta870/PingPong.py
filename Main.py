from turtle import  Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
#Set up the screen
screen= Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(1200,900)
screen.tracer(0)

#Create paddles, ball and score
r_paddle = Paddle((570,0))
l_paddle = Paddle((-570,0))
ball = Ball()
score = Score()

#Control the paddles
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

#Main game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect the collision with the wall
    if ball.ycor() > 430 or ball.ycor() < -430:
        ball.bounce_y()

    # Detect the collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 535 or ball.distance(l_paddle) < 50 and ball.xcor() > -535:
        ball.bounce_x()

    #Detect when ball passes the wall
    if ball.xcor() > 590:
        score.l_point()
        ball.reset()
    if ball.xcor() < -590:
        score.r_point()
        ball.reset()


screen.exitonclick()