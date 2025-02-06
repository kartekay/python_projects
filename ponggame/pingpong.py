from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from pongscore import Scoreboard
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong")
screen.tracer(0)
r_paddle=(350,0)
l_paddle=(-350,0)
paddle1=Paddle(r_paddle)
paddle2=Paddle(l_paddle)
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(paddle1.go_up,"Up")
screen.onkey(paddle1.go_down,"Down")
screen.onkey(paddle2.go_up,"w")
screen.onkey(paddle2.go_down,"s")
game_on=True
while game_on is True:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor()>=280 or ball.ycor()<=-280:
        ball.bounce()
    if ball.xcor()>=340 and ball.distance(paddle1)<=50:
        ball.collide()
    if ball.xcor()<=-340 and ball.distance(paddle2)<=50:
        ball.collide()
    if ball.xcor()>=380:
        score.lscore+=1
        score.update()
        ball.reset()
    if ball.xcor()<=-380:
        score.rscore+=1
        score.update()
        ball.reset()










screen.exitonclick()