def solution(citations):
    n = len(citations)
    while n > 0:
        count = 0

        for citation in citations:
            if citation >= n:
                count += 1

        if count >= n:
            break
        n -= 1

    return n


### 다른 사람 풀이
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer