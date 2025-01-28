from turtle import Turtle,Screen


from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon name",["Pikachu","Squirtle","Charizard"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)

class User:
    def __init__(self):
        self.followers=0
user_one=User()
user_one.username="luffy"
user_one.followers=10000
print(user_one.followers)
