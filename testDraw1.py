import turtle 

terry = turtle.Turtle()

terry.speed(1)
terry.color("blue", "cyan")
#terry.width(2)
terry.pensize(5)


#turtle.screensize(2000,1500)
print(turtle.window_height())
print(turtle.window_width())


terry.setheading(90)
terry.forward(50)
terry.color("orange")
for i in range(4):
	terry.forward(10)
	terry.left(20)
	
turtle.done()