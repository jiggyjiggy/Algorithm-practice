# 이건 그냥 함수 호출 순서 확인 해보는 코드
# memoization으로 구현한 fibo

d = [0] * 100

def fibo(x):
    print("f" "(" + str(x) + ")", end=" ") # f(x) 들을 공백기준 출력

    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

fibo(70)