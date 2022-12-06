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


### 타인 풀이
def solution(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


### hash 사용
def solution(phone_book):
    answer = True
    hash_map = {phone_number: 1 for phone_number in phone_book}

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if (temp in hash_map) and (temp != phone_number):
                answer = False
    return answer
