from turtle import Turtle,Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
snake=Snake()
scoreboard=Scoreboard()
food=Food()
screen=Screen()
screen.setup(600,600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



game_on=True
while game_on is True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
       food.refresh()
       snake.extend()
       scoreboard.increase_score()
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor() <-300:
        game_on=False
        scoreboard.gameover()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            scoreboard.gameover()

























screen.exitonclick()