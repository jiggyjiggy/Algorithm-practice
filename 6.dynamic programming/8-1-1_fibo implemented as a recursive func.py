# just fibo func. not a dynamic programming
# fibo 숫자 커지면 계산 엄청 오래걸림

# recursive
# top-down

def fibo(x):
    if (x == 1) or (x == 2):
        return 1
    return fibo(x - 1) + fibo(x - 2)

print("시작")
print(fibo(70))
print("끝")