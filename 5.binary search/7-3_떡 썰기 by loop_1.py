# 모범답안
n, m = map(int, input().split())
array = list(map(int, input().split()))

# binary search를 위한 start_idx, end_idx
start = 0
end = max(array)    # list를 sort 후 마지막 원소를 뽑을 필요 없이 max 함수로 처리

result = 0
while (start <= end):
    total = 0
    mid = (start + end) //
    for x in array:
        if x > mid:
            total += x -mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)