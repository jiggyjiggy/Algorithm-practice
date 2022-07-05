def solution(s):
    shift = 0
    for i in len(s):


    answer = 0
    return answer


###
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 입력예시
# "aabbaccc"

# 출력예시
# 7

# 모범답안
def solution(s):
    answer = len(s)
    for step in range(1, len(s) // 2 +1):
        compressed = ""
        prev =s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[s:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
            compressed += str(count) + prev if count >= 2 else prev
            answer = min(answer, len(compressed))
        return answer
###
