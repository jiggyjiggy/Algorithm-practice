# https://school.programmers.co.kr/learn/courses/30/lessons/42586

### 내 풀이
# 구현 으로 푼 느낌임
import math


def solution(progresses, speeds):
    target_list = []
    return_idx = 0
    answer = [0] * len(progresses)

    for i in range(len(progresses)):
        rest = 100 - progresses[i]

        target_list.append(math.ceil(rest / speeds[i]))

    publish_day = target_list[0]

    for target in target_list:

        if target > publish_day:
            publish_day = target
            return_idx += 1

        answer[return_idx] += 1

    answer = answer[:return_idx + 1]
    return answer
###

### 다른사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
###