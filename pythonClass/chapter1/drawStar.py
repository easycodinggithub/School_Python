import turtle as t

def draw(x, y):
    t1.goto(x, y)

t1 = t.Turtle()
t1.pensize(10)
t.onscreenclick(draw)

# t.onkey(t.penup, "up")
# t.onkey(t.penup, "Down")
# t.listen()

# turtle 실행
t.mainloop()

# turtle 종료
t.bye()