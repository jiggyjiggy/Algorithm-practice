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