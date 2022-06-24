data = input()

zero_group=0
one_group=0

for idx, value in enumerate(data):
    if idx == len(data) - 1:
        if value == '0':
            zero_group += 1
        if value == '1':
            one_group += 1
        break

    if value != data[idx + 1]:
        if value == '0':
            zero_group += 1
        if value == '1':
            one_group += 1

result = min(zero_group, one_group)
print(result)


# ###
# # 입력예시
# # 0001100
# #
# # 출력예시
# # 1
#
# # 모범답안
# data = input()
# count0 = 0
# count1 = 0
#
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(data) - 1):
#     if data[i] != data[i + 1]:
#         if data[i + 1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0, count1))
# ###