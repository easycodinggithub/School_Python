# turtle 사용

import turtle

# turtle 시작
t = turtle.Turtle()

# turtle의 모양 설정
t.shape("turtle")

# 100만큼 앞으로 이동
t.forward(100)
# 왼쪽으로 120도 이동
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)

# turtle 실행
turtle.mainloop()

# turtle 종료
turtle.bye()