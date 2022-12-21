# turtle로 정사각형 그리기

import turtle

t = turtle.Turtle()
t.shape("turtle")

def drawSquare(width, count):
    for i in range(count):
        for j in range(4):
            t.forward(width)
            t.left(90)
        x, y = t.position()
        t.up()
        t.goto(x+110, y)
        t.down()

width = int(input("정사각형 한변의 길이를 입력하세요: "))
count = int(input("그릴 정사각형 수를 입력하세요: "))

drawSquare(width, count)

turtle.mainloop()
turtle.bye()