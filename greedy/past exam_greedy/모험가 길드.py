from collections import deque

n = int(input())
traveler = list(map(int, input().split()))

traveler.sort()
traveler = deque(traveler)

# 공포도 제일 높은 여행자 고르고 그 수에 맞게 배치
all_group = []

while traveler:
    target = traveler.pop()
    group = []
    for _ in range(target-1):
        group.append(traveler.popleft())
    group.append(target)
    all_group.append(group)

print(len(all_group))