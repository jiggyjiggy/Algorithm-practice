# min() 함수 사용 예시
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)   # 받은 값에서 작은 수 저장
    result = max(result,min_value)  # 작은수 중 가장 큰 수 // 첫번쨰 : 0, min_value 비교 후 큰 값 result에 저장

print(result)

#
# Q. max 함수에서 result parameter를 빼면 for 구문이 1번만 실행되어 1행 입력후 err발생.
#
# >>> help(max)
# Help on built-in function max in module builtins:
#
# max(...)
#     max(iterable, *[, default=obj, key=func]) -> value
#     max(arg1, arg2, *args, *[, key=func]) -> value
#
# 즉 최소 인자 2개 받는거다
# min()에서도 똑같은데 data가 list_assignment_and_print_methods object다