# from collections import deque
#
# n = int(input())
# traveler = list(map(int, input().split()))
#
# traveler.sort()
# traveler = deque(traveler)
#
# # 공포도 제일 높은 여행자 고르고 그 수에 맞게 배치
# all_group = []
#
# while traveler:
#     target = traveler.pop()
#     group = []
#     for _ in range(target-1):
#         group.append(traveler.popleft())
#     group.append(target)
#     all_group.append(group)
#
# print(len(all_group))

###
n = int(input())
travelers_fearness = list(map(int, input().split()))

travelers_fearness.sort()

max_group = 0
count = 0

for traveler_fearness in travelers_fearness:
    count += 1
    if traveler_fearness <= count:
        max_group += 1
        count = 0

print(max_group)
###


###
# 해설
n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
###