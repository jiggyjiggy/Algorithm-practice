# 2중 반복문 구조 사용 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001   # 카드 숫자는 10000 이하의 자연수 입력 받는 중 
    for a in data:
        min_value = min(min_value, a)    # min_value와 각 row별 element 순회하면서 비교
    result = max(result, min_value)

print(result)