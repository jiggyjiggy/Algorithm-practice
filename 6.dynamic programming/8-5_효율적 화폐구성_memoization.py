n, m = map(int, input().split())

target = []
for i in range(n):
    target.append(int(input()))

memo = [10001] * (m + 1)

memo[0] = 0
for i in range(n):
    for j in range(target[i], m + 1):
        if memo[j-target[i]] != 10001:
            memo[j] = min(memo[j],memo[j-target[i]] + 1)

if memo[m] == 10001:
    print(-1)
else:print(memo[m])