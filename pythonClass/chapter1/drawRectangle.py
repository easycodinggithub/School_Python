import turtle as t
# x, y에서 가로w 세로h, 색깔color 네모 그리기
def qua(x, y, w, h, color):
    t1.ht()
    t1.speed(8)
    t1.up()
    t1.goto(x, y)
    t1.down()
    t1.color(color)
    t1.begin_fill()
    for i in range(2): #사각형 모양
        t1.fd(w)
        t1.lt(90)
        t1.fd(h)
        t1.lt(90)
    t1.end_fill()
t1 = t.Turtle()
qua(-100, -100, 200, 200, "red")
