import turtle as t

def t_up():
    t1.seth(90)
    t1.forward(10)

def t_down():
    t1.seth(270)
    t1.forward(10)

def t_right():
    t1.seth(0)
    t1.forward(10)

def t_left():
    t1.seth(180)
    t1.forward(10)

t1=t.Turtle()
        t1.pensize(10)

t.onkey(t_up, "Up")
t.onkey(t_down, "Down")
t.onkey(t_right, "Right")
t.onkey(t_left, "Left")

t.listen()

# turtle 실행
t.mainloop()

# turtle 종료
t.bye()