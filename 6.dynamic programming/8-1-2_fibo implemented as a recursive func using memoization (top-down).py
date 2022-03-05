# dynamic programming
# recursive
# top-down
# memoization

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:   # 2. memoization logic이 적용되는 부분 / 저장값이 존재하면 호출
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)    # 1. 아하 memoization은 x > 5 이상부터 memoization logic이 적용되는구나~!

    return d[x]

print('시작')
print(fibo(4))
print('끝')