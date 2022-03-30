from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('blue')
    circle(i)
    color('white')
    circle(i*0.8)
    right(1)
    forward(1)
    right(2)
    forward(3)
done()
