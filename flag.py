import turtle

turtle.begin_fill()

turtle.color("green")



#Triangle Shape

turtle.shape("triangle")

turtle.forward(400)

turtle.left(90)

turtle.forward(200)

turtle.left(90)

turtle.forward(400)

turtle.left(90)

turtle.forward(200)

turtle.end_fill()



#Make position for circle

turtle.color("red")

turtle.left(90)

turtle.forward(250)

turtle.left(90)

turtle.penup()

turtle.forward(100)

turtle.pendown()



#Make Circle

turtle.begin_fill()

turtle.circle(50)

turtle.end_fill()



#Bamboo



turtle.color("yellow")

turtle.right(90)

turtle.penup()

turtle.forward(150)

turtle.pendown()

turtle.right(90)

turtle.forward(100)

turtle.right(90)

turtle.forward(400)

turtle.left(90)



turtle.begin_fill()

turtle.forward(250)

turtle.left(90)

turtle.forward(10)

turtle.left(90)

turtle.forward(250)

turtle.end_fill()







turtle.exitonclick()