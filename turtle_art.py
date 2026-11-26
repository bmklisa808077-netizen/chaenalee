import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("무지개 꽃 만다라")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)
turtle.tracer(2)

n = 36
for i in range(n):
    t.color(colorsys.hsv_to_rgb(i / n, 1, 1)) 
    for _ in range(2):         
        t.circle(150, 60)
        t.left(120)
    t.left(360 / n)           

# 2) 바깥쪽 점 테두리
t.penup()
for i in range(72):
    t.goto(0, 0)
    t.setheading(i * 5)
    t.forward(190)
    t.dot(6, colorsys.hsv_to_rgb(i / 72, 1, 1))


t.goto(0, -25)
t.setheading(0)
t.pendown()
t.color("gold")
t.begin_fill()
t.circle(25)
t.end_fill()

turtle.update()
turtle.done()