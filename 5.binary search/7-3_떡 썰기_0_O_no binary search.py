n, m = map(int, input().split())
rice_length = list(map(int, input().split()))
rice_length.sort()
max = rice_length[-1]
result = 0
target = [0] * n

while result < m:
    for idx, value in enumerate(rice_length):
        if max == value:
            target[idx] += 1
            rice_length[idx] -= 1
    max -= 1
    result = sum(target)
print(max)