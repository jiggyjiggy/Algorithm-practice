n, to_go_rice = map(int, input().split())
rice_length = list(map(int, input().split()))

start_idx = 0
end_idx = max(rice_length)

result = 0

while (start_idx <= end_idx):
    mid_idx = (start_idx + end_idx) // 2
    cutting_rice = 0

    for each_length in rice_length:
        if each_length > mid_idx:
            cutting_rice += each_length - mid_idx

    if cutting_rice >= to_go_rice:
        result = mid_idx
        start_idx = mid_idx + 1
    else:
        end_idx = mid_idx - 1

print(result)
