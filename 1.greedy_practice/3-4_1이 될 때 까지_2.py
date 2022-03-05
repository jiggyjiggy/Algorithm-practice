# n, k 공백으로 구분하여 입력받기
#
# n이 k될때까지 1씩 뺀다(반복문)
# n // k
# 근데 n < k으면 반복문 탈출
#
# 남은 수에 대해 -1
#
# 실행횟수 카운팅

n, k = map(int, input().split())

count = 0

while True:
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k:
        break

    count += 1
    n //= k

count += (n - 1)
print(count)




