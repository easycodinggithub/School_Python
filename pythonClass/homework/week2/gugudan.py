# 2. 2단부터 19단까지의 구구단표를 출력하는 프로그램을 작성하세요.
# 형식은 다른 사람이 봤을 때 19단 구구단표라는 것을 알 수 있으면 됩니다.

def gugudan():
    for j in range(2, 20):
        print("--- %d단 ---" % j)
        for i in range(1, 10):
            print("%d * %d = %d" % (j, i, j*i))

gugudan()
