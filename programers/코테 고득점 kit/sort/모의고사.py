###
# def solution(answers):
#     rule1 = [1,2,3,4,5] * 10000
#     rule2 = [2,1,2,3,2,4,2,5] * 10000
#     rule3 = [3,3,1,1,2,2,4,4,5,5] * 10000

#     count1 = 0
#     count2 = 0
#     count3 = 0

#     for idx, answer in enumerate(answers):
#       if rule1[idx] == answer:
#         count1 += 1
#       if rule2[idx] == answer:
#         count2 += 1
#       if rule3[idx] == answer:
#         count3 += 1

#     target = []

#     target.append((1, count1))
#     target.append((2, count2))
#     target.append((3, count3))

#     aaaaa = sorted(target, key=lambda count: count[1], reverse=True)

#     zzz =[]
#     for num, count in aaaaa:
#         if count != 0:
#             zzz.append(num)

#     return zzz

def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0, 0]
    result = []

    for idx, ans in enumerate(answers):
        if s1[idx % len(s1)] == ans:
            score[1] += 1
        if s2[idx % len(s2)] == ans:
            score[2] += 1
        if s3[idx % len(s3)] == ans:
            score[3] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx)

    return result
###