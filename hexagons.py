import turtle
t=turtle.Pen()
t.speed(0)
t.pensize(5)
screen=t.getscreen()
screen.bgcolor('black')
colors=['red','blue','purple','green','yellow']
for i in range(10):
    for i in range(5):
        t.color(colors[i])
        t.fd(100)
        t.lt(360/5)
    t.lt(36)


    
