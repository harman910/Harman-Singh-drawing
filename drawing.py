import turtle
import random

t = turtle.Turtle()

# Set the speed of the turtle
t.speed(10)

# Define colors
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


for i in range(360):
    t.pencolor(colors[i % len(colors)])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

# Hide the turtle and display the final result
t.hideturtle()
turtle.done()
