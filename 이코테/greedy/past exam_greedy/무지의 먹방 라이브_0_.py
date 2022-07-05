# def solution(food_times, k):
#     iter = sum(food_times)
#     length = len(food_times)
#     zero_count = 0
#     limit = 0
#     if iter >= k:
#         for i in range(k+1):
#             if i >= length:
#                 loop = length // i
#                 if loop == 1:
#                     limit += 1
#             loop_idx = i - length * limit
#             if food_times[loop_idx] == 0:
#                 zero_count += 1
#                 pass
#             else:
#                 food_times[loop_idx] -= 1
#         answer = loop_idx + zero_count + 1 - length * limit
#     else:
#         answer = -1
#
#     return answer
#
# print(solution([3, 1, 2], 5))



###
# https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3
# 입력예시
# [3, 1, 2], 5
#
# 출력예시
# 1

# 모범답안
import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + (((q[0][0]) - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]
###