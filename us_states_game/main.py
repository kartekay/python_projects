from turtle import Screen, Turtle
import turtle
import pandas as pd
screen=Screen()
screen.setup(width=700,height=600)
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
tim=Turtle()
game_on=True
data=pd.read_csv("50_states.csv")
a=data.state.to_list()
b=data.x.to_list()
c=data.y.to_list()

while game_on is True:
   answer_state=screen.textinput(title="Guess the state",prompt="What's another state")
   if answer_state in a:
       d=a.index(answer_state)
       tim.goto(b[d],c[d])
       tim.pendown()
       tim.write(answer_state)
       tim.penup()













screen.exitonclick()