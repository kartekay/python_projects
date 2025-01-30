import random
from turtle import Turtle,Screen
colors=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction=[100,90,75,15,85,70,60,80,45,35,30,20,25,50,55,65,60,40,270,180,320,127,155]
tim=Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed("fastest")
tim.circle(100)
for i in range(3,11):
  for j in range(0,i):
    tim.forward(100)
    tim.left(360/i)
for k in range(10):
    tim.forward(10)
    tim.setheading(random.choice(direction))
tim.forward(100)
for i in range(10):
 tim.pendown()
 tim.forward(10)
 tim.penup()
 tim.forward(10)
tim.clear()
tim.home()
tim.pendown()
angles=[45,90,75,15,35,55]
for x in range(72):
    tim.circle(100)
    tim.right(5)


screen=Screen()
screen.exitonclick()