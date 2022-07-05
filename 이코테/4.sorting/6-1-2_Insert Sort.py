array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # index 0은 정렬된 것으로 간주하고 index 1부터 검사 시작
    for j in range(i, 0, -1):   # i 부터 왼쪽으로 하나씩 순회
        if array[j] < array[j-1]:   # target이 왼쪽 value보다 작다면
            array[j] ,array[j-1] = array[j-1] ,array[j] # swap
        else:   # target이 왼쪽 value보다 작지 않다면 / 그 이전 과정에서 이미 오름차순 sorting되어있음
            break   # 따라서 해당 그룹 검사 탈출

print(array)