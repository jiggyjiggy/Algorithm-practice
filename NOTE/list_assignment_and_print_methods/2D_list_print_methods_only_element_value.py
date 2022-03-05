# for문 1번
for _ in matrix:
    print(_)

for x,y, ... in matrix: # 각 길이가 다른 2중 리스트에선 안됌. 행렬에서라면 inner_element 갯수에 맞춰 변수 설정해야함
    print(x, y, ...)


# for문 2번, list의 iterator 이용
for element in matrix:    # 2중 list에서 각 element(각 list_assignment_and_print_methods object)(각 row)에 대해
    for inner_element in element: # element의 inner element를
        print(inner_element, end=' ')   # 공백을 기준으로 element value 자체를 출력한다
    print() # 하나의 row(inner_element) 출력 후 \n처리


# for문 2번, range 사용
for i in range(len(matrix)):    # 2중 list에서 element 갯수 = 세로 크기 (row의 갯수)
    for j in range(len(matrix[i])): # element의 inner_element 갯수 = 가로 크기 (column의 갯수)
        print(matrix[i][j], end=' ')    # 공백을 기준으로 element value 자체를 출력한다
    print() # 하나의 row(inner_element) 출력 후 \n처리


# while문 1번
row = 0   # 0번째 element부터 올라가기위해 변수 assign
while row < len(matrix):  # list_assignment_and_print_methods element 갯수만큼 반복
    _ = matrix[row]   # element 자체를 통으로 assign (inner element 각각을 따로 저장하는게 아님)
    print(_)
    row += 1

    # 다만 여러개의 args를 받는다 생각하여 *_를 변수로 assignment했음.
    # 오류가 났음
    >>> while row < len(matrix):
    ...     *_ = matrix[row]
    ...     print(*_)
    ...     row += 1
    ...
      File "<stdin>", line 2
    SyntaxError: starred assignment target must be in a list or tuple
    # *_는 list나 tuple 안에 있어야한다?
    # element를 통으로 받지 않고 그 내부에서 짤라서 받는다는 소리


# while문 2번
row = 0
while row < len(matrix):
    coulum = 0
    while j < len(matrix[row]):
        print(matrix[row][column], end=' ') # inner_element 각각을 출력, 공백 기준
        coulumn += 1
    print()
    row += 1