def solution(arr):
    answer = []
    answer.append(arr[0])
    for idx in range(1, len(arr)):
        if arr[idx - 1] != arr[idx]:
            answer.append(arr[idx])

    return answer


## 다른 사람 풀이 참고

# 결과를 담아둔 리스트의 마지막 값과 비교한다
# 이때 slicing 으로 리스트를 떠와야,
# 맨 처음 빈 리스트의 인덱싱 중에 안죽는다

def solution(arr):
    answer = []
    for item in arr:
        if answer[-1:] == [item]:
            continue
        answer.append(item)
    return answer



## 효율성은 위의 solution 이 좋다