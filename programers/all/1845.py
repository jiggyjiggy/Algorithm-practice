def solution(nums):
    length1 = len(nums) / 2
    length2 = len(set(nums))

    if length1 < length2:
        return length1
    return length2


## 다른사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
