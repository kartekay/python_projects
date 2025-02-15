import turtle
import random


screen = turtle.Screen()
screen.title("Turtle Minesweeper")
screen.bgcolor("lightgray")
screen.setup(width=600, height=600)


grid_size = 10
cell_size = 40
mines = []


for _ in range(15):
    x = random.randint(0, grid_size - 1)
    y = random.randint(0, grid_size - 1)
    if (x, y) not in mines:
        mines.append((x, y))


grid = {}
for i in range(grid_size):
    for j in range(grid_size):
        cell = turtle.Turtle()
        cell.shape("square")
        cell.color("white")
        cell.penup()
        cell.goto(-200 + j * cell_size, 200 - i * cell_size)
        grid[(i, j)] = cell


player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
player.goto(-200, 200)

player_pos = [0, 0]

def check_mine():
    if tuple(player_pos) in mines:
        for (x, y) in mines:
            grid[(x, y)].color("red")
        player.color("red")
        screen.title("Game Over! You hit a mine.")
        return True
    return False


def move_up():
    if player_pos[0] > 0:
        player_pos[0] -= 1
        player.sety(player.ycor() + cell_size)
        if check_mine(): return

def move_down():
    if player_pos[0] < grid_size - 1:
        player_pos[0] += 1
        player.sety(player.ycor() - cell_size)
        if check_mine(): return

def move_left():
    if player_pos[1] > 0:
        player_pos[1] -= 1
        player.setx(player.xcor() - cell_size)
        if check_mine(): return

def move_right():
    if player_pos[1] < grid_size - 1:
        player_pos[1] += 1
        player.setx(player.xcor() + cell_size)
        if check_mine(): return


screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.mainloop()
