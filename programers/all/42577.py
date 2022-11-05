### 시간초과
def solution(phone_book):
    answer = True

    for idx, phone_i in enumerate(phone_book):
        for jdx, phone_j in enumerate(phone_book):

            if idx == jdx:
                continue

            if phone_j.startswith(phone_i):
                answer = False
                return answer

    return answer


