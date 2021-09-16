import random
import turtle
import time

a=turtle.Turtle()
sc=turtle.Screen()
sc.screensize(700,500)
sc.bgcolor("black")
a.color('yellow')
time.sleep(1)
a.write("STAR WARS",True,align="center", font=("Arial", 38, "normal"))
time.sleep(1)
sc.clear()
sc.tracer(50)
sc.bgcolor("black")
a.shape('circle')
size=[1,2,3,4]
for i in range(1700):
    if i % 2 == 0:
        a.color("light blue")
    else:
        a.color("white")
    
    a.pensize(random.choice(size))
    distance = random.randint(20,700)
    angle = random.randint(0,360)
    a.rt(angle)
    
    a.up()
    a.fd(distance)
    a.down()
    
    line = distance / 10
    a.fd(line)
    
    a.up()
    a.goto(0,0)
    a.down()
    
