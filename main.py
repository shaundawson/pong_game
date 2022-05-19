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

    # TODO: Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    # TODO: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
       ball.bounce_x()

    # TODO: Detect when the ball goes out of bounds (right paddle)
    if ball.xcor() > 380:
        ball.reset_position()

    # TODO: Detect when the ball goes out of bounds (left paddle)
    if ball.xcor() < -380:
        ball.reset_position()

    
        
screen.exitonclick()



    


# TODO: Keep Score
