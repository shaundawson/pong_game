from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


# TODO: Set up the main screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
# TODO: Create another paddle
l_paddle = Paddle((-350, 0))
ball = Ball()


# TODO: Create paddle that responds to key presses
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()




# TODO: Create the ball and make it move
# TODO: Detect collision with wall and bounce
# TODO: Detect collisions with the the paddle
# TODO: Detect when the ball goes out of bounds
# TODO: Keep Score
