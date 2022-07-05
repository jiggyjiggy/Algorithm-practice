# 톱니형 리스트 (2D)

# 톱니형 리스트. 각기 다른 inner_element 갯수
# comprehension, for문에서 둘다 적용
column_element_numbers = [3, 1, 6, 3, 7]


# list_assignment_and_print_methods comprehension
dif_len_2D_list = [[[0] * column_element_number] for column_element_number in column_element_numbers]


# for문 2번, range사용
dif_len_2D_list = []

for _ in column_element_numbers:
    inner_list = []
    for column in range(_):
        inner_list.append(0)
    dif_len_2D_list.append(inner_list)
