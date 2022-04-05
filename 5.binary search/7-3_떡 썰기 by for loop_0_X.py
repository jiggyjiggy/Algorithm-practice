n, m = map(int, input().split())
rice_length = list(map(int, input().split()))

rice_length.sort()

start_idx = 0
end_idx = rice_length[-1]
mid_idx = (start_idx + end_idx) // 2

target = [0] * n


for each_length_idx, each_length in enumerate(rice_length):
    if (each_length - mid_idx) > 0:
        target[each_length_idx] = each_length - mid_idx

    while sum(target) < m:
    else:
        print(mid_idx)

###
# 흠,, 아님

