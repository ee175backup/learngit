from turtle import Turtle, Screen
import Tkinter
import Image

f = open('/home/pi/Desktop/datavalue1.txt','r')
data = f.read()
rows = data.split('\n')

full_data = []
for row in rows:
    split_row = row.split(",")
    size = len(split_row)
    if size == 4:
        
        split_row[0] = float(split_row[0])
        split_row[1] = float(split_row[1])
        split_row[2] = float(split_row[2])
        split_row[3] = float(split_row[3])
        full_data.append(split_row)

turtle1 = Turtle(shape = 'turtle')
turtle1.color("red")
turtle1.pensize(5)
turtle1.goto(0,0)
turtle1.speed(10)
turtle1.penup()
#turtle.screensize(200,150)

turtle2 = Turtle(shape = 'turtle')
turtle2.color("blue")
turtle2.pensize(5)
turtle2.goto(0,5)
turtle2.speed(10)
turtle2.penup()
#t.pendown()



for item in full_data:
    turtle1.pendown()
    #t1.left(item[1])
    #t1.forward(item[0])
    turtle1.left(item[1])
    turtle1.forward(item[0])
    turtle1.penup()

    turtle2.pendown()
    turtle2.left(item[2])
    turtle2.forward(item[3])
    turtle2.penup()



ts = turtle1.getscreen()
ts.getcanvas().postscript(file="Test1.eps")

im = Image.open('/home/pi/Desktop/Test1.eps')
im.save('/home/pi/Desktop/Test1.jpg/','JPEG')
