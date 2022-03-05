# binary search basic logic
# 1. 시작점, 끝점 설정 / 중간점(시작 끝 의 중간, 소숫점은 버림 <- " // " 몫 연산자 사용)
# 2. target과 중간점 위치에 있는 데이터를 반복적으로 비교
# 3. 비교점들을 재설정

# implemented as a recursive func
# 재귀로 구현시 종료조건 필수
# 시작점이 끝점보다 크면 종료
# 찾은경우 중간점 인덱스 리턴
# 중간점 값보다 target 값이 작은경우 왼쪽 검사
# 중간점 값보다 target 값이 큰 경우 오른쪽 검사

# 입력값:
# 1. 원소 갯수, 찾고자하는 data(이 문제에선 숫자)
# 2. 전체 원소

# 출력값:
#

def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int,input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("존재하지 않는 target")
else:
    print(result + 1)