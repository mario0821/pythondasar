import turtle 
def tangentcircle (ttl):
    """" print 10 tanget circle ."""
    r = 10 
    n = 10
    for i in range (1 , n + 1, 1) :
        ttl.circle (r*i)
        def concentricircles (ttl):
            """" print 10 consentric circles ."""
            r = 10 
            for i in range (10) :
                ttl.circle ( r * i)
                ttl.up()
                ttl.sety (( r * i) * ( -1))
                ttl.down()

Ben = turtle . Turtle ()
Ben.up() ; Ben.goto(0, 150)
Ben.down() ; Ben.pencolor("blue")
tangentcircle(Ben)
Ben.up() ; Ben.goto(0 , -150)
Ben.down() ; Ben.pencolor("red")
concentricircles(Ben)
