# 집 혹은 가게를 기준으로 거리1씩 늘리면서(?) [둘러싸는 사각형] 서치하려했으나
# 가게 혹은 집의 위치를 저장하면 될듯?
# 집 ~ 가게 조합?의 경우의 수만큼 거리 계산 (완전탐색) ;
# 가게 기준 집 거리를 비교해서 (초기: 무한대) 작은 거리로 갱신

n, m = map(int, input().split())

houses = []
stores = []

length_list_per_stores = []

for row in range(n):
    data = list(map(int, input().split()))
    for column in range(n):
        if data[column] == 1:
            houses.append((row, column))
        elif data[column] == 2:
            stores.append((row, column))

for store in stores:
    store_row, store_column = store

    length_list = []
    for house in houses:
        house_row, house_column = house

        road_length = (abs(house_row - store_row) + abs(house_column - store_column))
        length_list.append(road_length)
    sum_road_length = sum(length_list)
    # sum_road_length = 가게의 치킨거리
    # 가게 마다의 치킨거리 비교를 위해
    length_list_per_stores.append(sum_road_length)
length_list_per_stores.sort()
result = sum(length_list_per_stores[:m])
print(result)
###



# ###
# # 입력예시 1
# # 5 3
# # 0 0 1 0 0
# # 0 0 2 0 1
# # 0 1 2 0 0
# # 0 0 1 0 0
# # 0 0 0 0 2
# #
# # 출력예시 1
# # 5
#
# # 입력예시 2
# # 5 1
# # 1 2 0 0 0
# # 1 2 0 0 0
# # 1 2 0 0 0
# # 1 2 0 0 0
# # 1 2 0 0 0
# #
# # 출력예시 2
# # 10
#
# # 모범답안
# from itertools import combinations
#
# n, m = map(int, input().split())
# chicken, house = [], []
#
# for r in range(n):
#     data = list(map(int, input().split()))
#     for c in range(n):
#         if data[c] == 1:
#             house.append((r, c))
#         elif data[c] == 2:
#             chicken.append((r, c))
#
# candidates = list(combinations(chicken, m))
#
# def get_sum(candidate):
#     result = 0
#
#     for hx, hy in house:
#         temp = 1e9
#         for cx, cy in candidate:
#             temp = min(temp, abs(hx - cx) + abs(hy - cy))
#         result += temp
#     return result
#
# result = 1e9
# for candidate in candidates:
#     result = min(result, get_sum(candidate))
#
# print(result)
# ###