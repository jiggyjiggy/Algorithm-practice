### 1
# n, m = map(int, input().split())
#
# target = []
# for i in range(n):
#     target.append(int(input()))
# target.sort()
#
# d = [0] * 100000
# for i in target:
#     d[i-1] = 1
#
# for j in range(2, m):
#     # 제일 큰 화폐 전 단계가 있다면
#     if d[j] != 0:
#         if j-target[j-3] > 0:
#             d[j] = d[j-target[j-3]] + 1
#     # 그 다음 큰 화폐
#     # d[i] = d[i - target[-2]] + 1
#     # 없다면
# if d[m] ==0:
#     print(-1)
# else:
#     print(d[j])


### 2
n, m = map(int, input().split())

result = [0] * 100
for i in range(n):
    target = int(input())
    result[target-1] = 1

for idx, value in enumerate(result):
    if result[idx] != 0:
        result[] += 1

print(result)

print(result[m-1])




