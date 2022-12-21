while True:
    originPrice = input("정가를 입력하시오 : ")
    if int(originPrice) >= 100:
        print("10층에서 사은품을 받아가세요.")
        print("할인된 가격= %d \n" % (int(originPrice) - int(originPrice) * 15 / 100))
    else:
        print("할인된 가격= %d \n" % (int(originPrice) - int(originPrice) * 15 / 100))

