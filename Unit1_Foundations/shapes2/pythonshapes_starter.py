from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

pendown()

for i in range(3):
    forward(100) # go forward 100 steps
    right(360/3)




# Close window on click.
exitonclick()
