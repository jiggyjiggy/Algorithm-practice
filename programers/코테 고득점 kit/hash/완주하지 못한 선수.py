def solution(participant, completion):
    dict_participant = {name : 0 for name in participant}
    for name in participant:
        if name in dict_participant.keys():
            dict_participant[name] += 1

    for name in completion:
        if name in dict_participant.keys():
            dict_participant[name] -= 1

    target = {v:k for k,v in dict_participant.items()}
    answer = target.get(1)
    return answer


###
# 다른 사람 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
###