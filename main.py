from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.bgcolor('blue')
screen.setup(800,600)
screen.title('Pong')
screen.tracer(0)
right_paddle = Paddle(360)
left_paddle = Paddle(-360)
# screen.update()



screen.listen()
screen.onkey(right_paddle.move_up, 'Up')
screen.onkey(right_paddle.move_down, 'Down')
screen.onkey(left_paddle.move_up, 'w')
screen.onkey(left_paddle.move_down, 's')


ball = Ball()
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect paddle collision (right)
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()



screen.exitonclick()
