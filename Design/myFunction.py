def tear(t):
    for times in range(10):
        c=(255,25,15)
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("black")
    polygon(t,7,25)
    t.color("orange")
    polygon(t,6,25)

def jump(t,x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def polygon_nc(t,sides,distance):
    angle = 360 / sides
    for times in range(sides):
        t.forward(distance)
        t.left(angle)

def flower(t,size):
    for times in range(10):
        t.left(times*36)
        tears(t,size)
        t.penup()
        t.home()
        t.pendown()

def tears(t,size):
    t.width(1)
    for times in range(10):
        t.begin_fill()
        c=(0,225,120)
        t.color(c)
        t.circle(times*2)
        t.left(10)
        t.forward(size)
        t.end_fill()

def star(t,distance):
    t.begin_fill()
    for times in range(6):
        t.forward(distance)
        t.left(72)
        t.forward(distance)
        t.right(144)

def triangle(w):
    for times in range(255):
        w1=(255-times,255-times,255-times)
        w.color(w1)
        w.forward(times*1.8)
        w.left(120)
        w.forward(times*1.8)
        w.left(120)
        
def square(x,y):
    for times in range(4):
        x.forward(y)
        x.left(90)

def circle(t,size):
    for times in range(90):
        t.left(4)
        t.circle(size)
        



    
