import turtle
turtle.bgcolor("black")
turtle.speed(10)
turtle.pensize(3)

while(True):
  for i in range(6):
    for colors in ["red", "blue", "yellow", "green"]:
     turtle.color(colors)
     turtle.circle(100)
     turtle.left(10)