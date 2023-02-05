import turtle

# Set the screen and turtle dimensions
turtle.setup(width=400, height=200)

# Set the background color to white
turtle.bgcolor("white")

# Create a turtle object
flag = turtle.Turtle()

# Speed up the turtle movement
flag.speed(10)

# Set the fill color to red
flag.fillcolor("red")

# Begin filling the red triangle
flag.begin_fill()

# Move the turtle to the top-left corner of the flag
flag.penup()
flag.goto(-150, 100)
flag.pendown()

# Draw the red triangle
flag.left(60)
flag.forward(300)
flag.right(120)
flag.forward(300)
flag.right(120)
flag.forward(300)

# End filling the red triangle
flag.end_fill()

# Set the fill color to white
flag.fillcolor("white")

# Begin filling the white diamond
flag.begin_fill()

# Move the turtle to the center of the flag
flag.penup()
flag.goto(0, 0)
flag.pendown()

# Draw the white diamond
for i in range(4):
    flag.forward(150)
    flag.right(90)

# End filling the white diamond
flag.end_fill()

# Hide the turtle
flag.hideturtle()

# Keep the screen open until it is closed
turtle.done()
