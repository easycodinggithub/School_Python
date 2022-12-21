def getIntRange(a, b=0):
    if a < 1 or a >12:
        getIntRange(int(input("월을 입력하세요(1부터 12사이의 값) :")))
        return
    else:
        m31 = [1,3,5,7,8,10,12]
        m30 = [4,6,9,11]
        if a in m31:
            b = int(input("일을 입력하세요(1부터 31사이의 값) :"))
            if b < 1 or b > 31:
                getIntRange(a, int(input("일을 입력하세요(1부터 31사이의 값) :")))
                return
        elif a in m30:
            if b < 1 or b > 30:
                getIntRange(a, int(input("일을 입력하세요(1부터 31사이의 값) :")))
                return
        elif a == 2:
            if b < 1 or b > 28:
                getIntRange(a, int(input("일을 입력하세요(1부터 31사이의 값) :")))
                return
        else:
            return
    print(f"입력된 날짜는 {a}월 {b}일 입니다.")
    return

getIntRange(int(input("날짜를 입력하세요.(월과 일)\n월을 입력하세요(1부터 12사이의 값) :")))