from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for position in starting_positions:
            newsegment = Turtle("square")
            newsegment.color("white")
            newsegment.penup()
            newsegment.goto(position)
            self.segments.append(newsegment)
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_distance)
    def extend(self):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(self.segments[-1].position())
        self.segments.append(newsegment)
    def up(self):
      if self.head.heading()!=DOWN:
        self.head.setheading(UP)
        self.head.forward(move_distance)
      else:
          pass
    def down(self):
      if self.head.heading()!=UP:
        self.head.setheading(DOWN)
        self.head.forward(move_distance)
      else:
          pass
    def left(self):
      if self.head.heading()!=RIGHT:
        self.head.setheading(LEFT)
        self.head.forward(move_distance)

      else:
          pass
    def right(self):
      if self.head.heading()!=LEFT:
        self.head.setheading(RIGHT)
        self.head.forward(move_distance)
      else:
         pass