import turtle as tt

# curve as 10(relative)
tt.bgcolor('black')
tt.pensize(2)
tt.speed(10)

for i in range (6) :

    for color in ('red', 'magneta', 'blue', 'cyan', 'green', 'white', 'yellow'):
     tt.color(color)

    tt.circle(100)

    tt.left(10)


    tt.hideturtle()