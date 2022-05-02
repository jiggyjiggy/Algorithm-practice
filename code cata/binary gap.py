def solution(N):
    count = 0
    max_count = 0
    target = list(bin(N)[2:])
    for i in target:
        if i == '0':
            count += 1
        if i == '1':
            if count > max_count:
                max_count = count
            count = 0
    return max_count