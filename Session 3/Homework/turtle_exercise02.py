from turtle import *
import turtle

colors = ["red", "blue", "brown", "yellow", "grey"]


for i in range(5):
    color(colors[i])
    turtle.begin_fill()
    turtle.down()
    for j in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    turtle.up()
    turtle.end_fill()
    forward(50)


mainloop()
