# 2중 for문으로 2중 list_assignment_and_print_methods 선언
# 열 하나 당 22개, element value가 0인 list_assignment_and_print_methods 선언
matrix = [[0 for column in range(22)] for row in range(11)]

# * operator와 for문으로 list_assignment_and_print_methods 선언
matrix = [[0]* 22 for _ in range(11)]
# 0이 1개 들어있는 list [0]에 22를 곱하면
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 이 되는데, 이걸 for _ in range(11)로 11번 반복하는 것
