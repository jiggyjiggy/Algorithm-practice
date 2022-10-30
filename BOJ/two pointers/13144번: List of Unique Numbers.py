import sys

si = sys.stdin.readline

n = int(si())
input_list = list(map(int, si().split()))
count_list = [0] * 100001

ans = 0
R = -1
for L in range(n):
    while (R + 1 < n) and (count_list[input_list[R + 1]] == 0):
        R += 1
        count_list[input_list[R]] = 1
    ans += R - L + 1
    count_list[input_list[L]] = 0

print(ans)
