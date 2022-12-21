while True:
    value = list(input().split(" "))

    a = int(value[0])
    b = int(value[1])
    if a <= 0 or a > b or b > 500:
        print("유효한 값이 아닙니다. ")
        break

    sum = 0

    for i in range(a, b + 1):
        if i % 2 == 0:
            print("- %d" % i, end=" ")
            sum -= i
        else:
            if i == a:
                print("%d" % i, end=" ")
            else:
                print("+ %d" % i, end=" ")
            sum += i
    print("= %d" % sum)

