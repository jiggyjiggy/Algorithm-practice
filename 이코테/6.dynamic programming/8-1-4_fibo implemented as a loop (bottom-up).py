# dynamic programming
# loop
# bottom-up
# DP table

d = [0] * 100

d[1] = 1
d[2] = 2
n = 70

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print('시작')
print(d[n])
print('끝')
