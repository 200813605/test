import turtle
from time import sleep, time
wn = turtle.Screen()
bob = turtle.Turtle()
bob.pencolor("orange")
wn.bgcolor("blue")

for i in range (3):
    bob.forward(200)
    bob.left(120)
for i in range(2):
    bob.forward(200)
    bob.right(120)
bob.forward(400)
bob.right(120)
bob.forward(400)
bob.right(120)
bob.forward(200)
bob.left(120)
bob.forward(200)
bob.left(120)
bob.forward(200)
bob.left(180)
bob.forward(400)
bob.right(120)
bob.forward(400)
bob.left(180)
bob.forward(200)
bob.left(120)
bob.forward(200)
bob.right(120)
bob.forward(200)
bob.right(120)
bob.forward(200)
print 'ART IS COMPLETE'
sleep(2)
