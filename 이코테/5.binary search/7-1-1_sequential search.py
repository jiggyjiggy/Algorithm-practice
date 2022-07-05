# 입력값:
# 1. 생성할 원소 갯수, 찾을 문자열, 공백을 기준  # 5 dongbin
# 2. 원소 갯수만큼의 문자열, 공백을 기준   # apple banana grade dongbin juice

# 출력값
# 1. sequential_search 로 찾은 인덱스

# sequential_search logic
# 각 원소를 하나씩 확인
# 현재의 원소가 찾고자 하는 원소와 동일한 경우
# 현재의 위치 반환

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))