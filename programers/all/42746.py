def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int("".join(numbers)))

# def sum(x, y):
#     return x + y
#
# res = sum(1,2)
#
# print(res)
#
# res2 = (lambda x,y : x + y) (1, 2)
# print(res2)
