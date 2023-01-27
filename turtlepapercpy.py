import turtle, random

window_width = 1920
window_height = 1080
turtle.bgcolor ("black")

t1 = turtle.Turtle ()
t2 = turtle.Turtle ()
t3 = turtle.Turtle ()

t1.hideturtle ()
t2.hideturtle ()
t3.hideturtle ()

t1.pencolor ("white")
t2.pencolor ("white")
t3.pencolor ("white")

t2.pensize (2)
t1.pensize (2)
t3.pensize (2)

t1.speed(0)
t2.speed(0)
t3.speed(0)

turtle.setup(window_width,window_height)

while True:
    
        direction = random.randint(0,1)
        t1.forward(15)

        if t1.xcor() < window_width/-2 \
        or t1.xcor() > window_width/2 or \
        t1.ycor() < window_height/-2 or \
        t1.ycor() > window_height/2:
            t1.penup()
            t1.goto(0,0)
            t1.setheading (0)
            t1.pendown()
        if direction == 0:
            t1.left(60)
        else:
            t1.right(60)

                
        direction = random.randint(0,1)
        t2.forward(15)

        if t2.xcor() < window_width/-2 \
        or t2.xcor() > window_width/2 or \
        t2.ycor() < window_height/-2 or \
        t2.ycor() > window_height/2:
            t2.penup()
            t2.goto(0,0)
            t2.setheading (0)
            t2.pendown()
        if direction == 0:
            t2.left(60)
        else:
            t2.right(60)

        direction = random.randint(0,1)
        t3.forward(15)

        if t3.xcor() < window_width/-2 \
        or t3.xcor() > window_width/2 or \
        t3.ycor() < window_height/-2 or \
        t3.ycor() > window_height/2:
            t3.penup()
            t3.goto(0,0)
            t3.setheading (0)
            t3.pendown()
        if direction == 0:
            t3.left(60)
        else:
            t3.right(60)