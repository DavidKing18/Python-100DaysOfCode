# HOW TO USE OOP CLASSES AND OBJECTS

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')
timmy.color('coral')
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Practice Modifying Object Attributes and Calling Methods

from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)
