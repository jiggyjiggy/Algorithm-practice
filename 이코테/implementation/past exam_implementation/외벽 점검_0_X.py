# # 외벽의 길이 n,
# # 취약 지점의 위치가 담긴 배열 weak,
# # 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때,
# # 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.
#
#
# ###
# def solution(n, weak, dist):
#     big = dist.pop()
#
#     x = 1e9
#     for p in weak:
#
#
#     if big > shift:
#
#
#     answer = 0
#     return answer
#
# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4]
# solution(n, weak, dist)
# ###

###
# https://programmers.co.kr/learn/courses/30/lessons/60062
# 입력예시
# n
# 12
# weak
# [1, 5, 6, 10]
# dist
# [1, 2, 3, 4]

# 출력예시
# 2

# 모범답안
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1

    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
solution(n, weak, dist)
###

# ###
# # programers 추천 답안 / 풀이자: - , zerowest , 구진범 , 정성환 , 성하연 외 6 명
# from collections import deque
#
# def solution(n, weak, dist):
#     dist.sort(reverse=True)
#     q = deque([weak])
#     visited = set()
#     visited.add(tuple(weak))
#     for i in range(len(dist)):
#         d = dist[i]
#         for _ in range(len(q)):
#             current = q.popleft()
#             for p in current:
#                 l = p
#                 r = (p + d) % n
#                 if l < r:
#                     temp = tuple(filter(lambda x: x < l or x > r, current))
#                 else:
#                     temp = tuple(filter(lambda x: x < l and x > r, current))
#
#                 if len(temp) == 0:
#                     return (i + 1)
#                 elif temp not in visited:
#                     visited.add(temp)
#                     q.append(list(temp))
#     return -1
# ###
