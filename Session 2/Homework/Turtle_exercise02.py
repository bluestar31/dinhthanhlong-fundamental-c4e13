from turtle import *

# for i in range(3):
#     forward(100)
#     left(120)
#
# for i in range(4):
#     forward(100)
#     left(90)
#
# for i in range(5):
#     forward(100)
#     left(72)
#
# for i in range(6):
#     forward(100)
#     left(60)



speed(-1)
for i in range(3,40):

    for a in range(i):
        if i % 2 == 0:
            color("red")
        else:
            color("blue")
        forward(100)
        left(360/i)
