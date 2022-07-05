def move_zeroes(nums):
    count = 0
    result = []
    for idx, i in enumerate(nums):
        if i == 0:
            count += 1

            result.append(idx)
    for j in result[:0]:
        del nums[j]

    for j in range(count):
        nums.append(0)

    return nums

move_zeroes([0,0,9,0,12])