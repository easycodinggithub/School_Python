import random as r

def sample(otp, n):
    r.shuffle(otp)
    return otp[:n]

otp = list(input("otp : "))
print(otp)
print(sample(otp, 4))