# n, k 공백으로 구분하여 입력받기

# n 이 k 보다 크면 우선 k로 계속 나누는게 빠름
#   나누어 떨어지지 않는다면 n - 1
# 나누어 떨어지면 n//k
#
# 마지막 남은 수가 1까지 1씩 뺸다
#
# 각 loop마다 count + 1

n, k = map(int, input().split())

count = 0

while n > k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)