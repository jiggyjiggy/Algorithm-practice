n, m = map(int, input().split())

target = []
for i in range(n):
    target.append(int(input()))

memo = [10001] * m

memo[0] = 0
for i in range(n):
    for j in range(target[i], m):
        if memo[j-target[i]] != 10001:
            memo[j] = min()