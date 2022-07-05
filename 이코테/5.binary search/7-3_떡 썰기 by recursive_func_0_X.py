n, m = map(int, input().split())
rice_length = list(map(int, input().split()))

rice_length.sort()

start_idx = 0
end_idx = rice_length[-1]

target = [0] * n

def binary_search(start_idx, end_idx, rice_length):
    mid_idx = (start_idx + end_idx) // 2
    for
        if sum(target) > m: # 자른 떡이, 가져가야할 떡보다 크면 우측 binary search
            start_idx = mid_idx + 1
            return binary_search(start_idx, end_idx, rice_length)
        elif sum(target) < m:
            end_idx = start_idx
            return binary_search(start_idx, end_idx, rice_length)
        elif sum(target) == m:





binary_search(start_idx, end_idx, rice_length)



