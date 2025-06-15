import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)

color_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (245, 232, 236), (118, 82, 93), (179, 140, 150),(41, 46, 65), 
(162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (238, 241, 245), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

timmy.speed("fastest")

timmy.setheading(225)
timmy.penup()
timmy.hideturtle()
timmy.forward(300)
timmy.setheading(0)

# timmy.pendown()

number_of_dots = 100

for dot_counts in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    
    if dot_counts % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)   



screen = t.Screen()
screen.exitonclick()