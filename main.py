from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# move paddle up

screen.listen()
# move right paddle up and down
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# move left paddle up and down
screen.onkeypress(left_paddle.move_up, "a")
screen.onkeypress(left_paddle.move_down, "z")

game_on = True

while game_on:
    time.sleep(0.025)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    # Change the ball's movement direction upon collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Detect collision with right paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.paddle_bounce()

    # Detect if paddle misses the ball and ball goes out of bounds at the edge of the screen
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()

    # When one of the players reaches a score of 10 the game ends
    if scoreboard.left_score == 10 or scoreboard.right_score == 10:
        game_on = False

screen.exitonclick()
