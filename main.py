from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

my_list = [0.1, 0]

screen = Screen()
screen.screensize(600, 400)
screen.bgcolor("black")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
r_paddle = Paddle((320, 0))
l_paddle = Paddle((-320, 0))
ball = Ball()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detecting the collision
    if ball.ycor() == 270 or ball.ycor() == -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 280 or ball.distance(l_paddle) < 50 and ball.xcor() < -280:
        ball.bounce_x()
        # time.sleep()

    # detect when right paddle misses
    if ball.xcor() > 300:
        ball.reset_position()
        scoreboard.track_lscore()

    if ball.xcor() < -300:
        ball.reset_position()
        scoreboard.track_rscore()






    

screen.exitonclick()


