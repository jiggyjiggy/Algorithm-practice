###
n, m = map(int, input().split())
data = list(map(int, input().split()))

memo = [0] * (m+1)
result = 0

for i in data:
    memo[i] += 1

for i in data:
    result += (sum(memo) - memo[i])
    memo[i] -= 1

print(result)
###






###
# 입력예시
# 5 3
# 1 3 2 3 2
#
# 출력예시
# 8

# 모범답안
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

for x in data:
    array[x] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)
###
