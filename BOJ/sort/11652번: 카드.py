import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))

a.sort()

mode = a[0]
mode_cnt = 1
cur_cnt = 1

for i in range(1, n):
    if a[i] == a[i - 1]:
        cur_cnt += 1
    else:
        cur_cnt = 1
    if mode_cnt < cur_cnt:
        mode_cnt = cur_cnt
        mode = a[i]

print(mode)
