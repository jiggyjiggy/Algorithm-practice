# 반복문으로 쓰면서 종료조건에 도달할 때 까지 반복 -> while로 진입

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid  # search 중 값 발견시 while 탈출
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split())) # import sys , input_data = sys.stdin.readline().rstrip() # 한줄씩 입력받음
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print('target이 존재하지 않음')
else:
    print(result + 1)
