#mianprogram
import turtle
from myFunction import * 
#imports everything from myFunctions


bob=turtle.Turtle()
bob.speed(0)
#fastest speed
turtle.bgcolor("black")


turtle.colormode(255)


flower(bob,150)
#function draws a flower with size 150


for times in range(90):
    bob.left(4)
    bob.color("sky blue")
    square(bob,150)
#draws a square that is sky blue and size 150


for times in range(90):
    bob.left(4)
    bob.color("light green")
    square(bob,175)
    


for times in range(90):
    bob.left(4)
    bob.color("purple")
    square(bob,200)


for times in range(90):
    bob.left(4)
    bob.color("yellow")
    square(bob,225)


for times in range(90):
    bob.left(4)
    bob.color("hot pink")
    square(bob,250)


for times in range(90):
    bob.left(4)
    bob.color("blue")
    square(bob,275)


for times in range(90):
    bob.left(4)
    bob.color("green")
    square(bob,300)


triangle(bob)
#function draws a triangle from white to black

