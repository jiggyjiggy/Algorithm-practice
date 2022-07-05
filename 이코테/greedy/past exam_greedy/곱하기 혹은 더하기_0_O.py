###
nums = input()

target = []
for i in range(len(nums)):
    target.append(nums[i])

result = int(target[0])
for idx, i in enumerate(target[1:]):
    idx +=1
    if nums[idx - 1] == '0':
        result += int(i)
    elif nums[idx - 1] == '1':
        result += 0
    else:
        result *= int(i)

print(result)
###

###
# 입력예시
# 02984
#
# 출력예시
# 576

# 모범답안
data = input()

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
###
