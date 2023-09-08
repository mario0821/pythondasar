import turtle 

# set up the turtle screen and set the bacground color to white
screen = turtle.screen ()
screen.bgcolor("white")
 
 # create a new turtle and set its speed to the fastest possible 
pen = turtle.screen ()
pen.speed (0)
 
pen.fillcolor("red")
pen.begin_fill ()

pen.circle(100)

pen.end_fill()
pen.hideturtle()

turtle.done ()