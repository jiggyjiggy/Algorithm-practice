array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # index i번부터 검사 시작
    min_index = i   # 비교할 그룹 중 최소 value를 저장 할 인덱스 선언 / 우선은 검사 시작 index를 할당해둠

    for j in range(i+1, len(array)):    # min_index 이후 인덱스들 / 끝 index까지 검사함
        if array[min_index] > array[j]: # 최소 value 인덱스에 저장된 값이 더 크다면
            min_index = j   # 최소 인덱스에 j 인덱스를 assign / 즉 두 값의 비교 후 작은 값의 index를 저장 한다는 뜻
    array[i], array[min_index] = array[min_index], array[i] # swap / # 한 그룹 비교 후 min_index 의 value로 저장된 값을, 검사 시작 index로 스왑

print(array)

'''

time complexity
O(N^2)

'''