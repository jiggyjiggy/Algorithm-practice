# position 변수를 list_assignment_and_print_methods object로 할당
position = []

# 1차원 list의 각 element에 list를 추가함으로써 2차원 list로 만듦
for i in range(19):
    # element 마다 리스트 선언
    position.append([])

    # i_n 에 대해 20(j) 반복
    for j in range(19):
        position[i].append(0)  # i_1 에대해 j_0~19 append /즉 하나의 row는 하나의 list_assignment_and_print_methods

for i in range(19):
    position[i] = list(map(int, input().split()))  # 따라서 \n을 기준으로 받는 map을 list로 선언해서 각 row로 assignment하는 것
