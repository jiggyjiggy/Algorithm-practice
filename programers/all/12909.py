def solution(s):
    count = 0

    for ch in s:
        if count < 0:
            return False
        count = count + 1 if ch == "(" else count - 1

    return count == 0
