import turtle

turtle.shape("turtle")
turtle.bgcolor("gray")
turtle.pensize(10)
turtle.up()
turtle.goto(-140, -20)
turtle.down()
# First 3 circle
turtle.color("blue")
turtle.circle(50)
turtle.up()
turtle.forward(130)
turtle.down()
turtle.color("black")
turtle.circle(50)
turtle.up()
turtle.forward(130)
turtle.down()
turtle.color("red")
turtle.circle(50)
#Second(1) circle
turtle.left(90)
turtle.up()
turtle.forward(50)
turtle.left(90)
turtle.forward(65)
turtle.down()
turtle.color("yellow")
turtle.circle(50)
#Second(2) circle
turtle.up()
turtle.forward(130)
turtle.down()
turtle.color("green")
turtle.circle(50)

turtle.exitonclick()