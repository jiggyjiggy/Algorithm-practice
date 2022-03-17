# # 1_X
# # 완전 틀림
# # 연결에 대한 확인 로직이 안떠올랐음
#
# # DFS로 연결되어있는 노드 판별
# # - 노드 정보 받기 / DFS적용하기 위해서는 -> "연결여부 정보" : 리스트의 인덱스대로 탐색 후 연속해서 0이면 저장?
# # 문제에서는 input은 노드의 정보만 줌 / edge?
# # - 방문 여부 저장
#
# # - DFS logic
# # 탐색하고자 하는 노드와 연결된 노드 방문(재귀) : 주변 탐색에 대해 점화식 구성 : 상하좌우 0인지 확인, 0이면 해당 노드 방문처리
# # 0,0에서 시작으로 강제하고
# # -> 방문했다면 탈출이니깐 (탈출조건)
# # -> 방문하지 않았다면 재귀
# # ---
#
# N, M = map(int, input().split())
#
# # matrix = [(list(map(int, input().split()))) for _ in range(N)]
# # 문제점: map객체를 list로 형변환 후 반복문으로 넣으니 0으로 시작하는 리스트는 0이 삭제됨
# # matrix: [[1], [10], [101]]
# # .split() 때문에 나타난 현상
# # 공백을 기준으로 받겟단 소리니, 숫자 한개 당 요소로 받지 않고 공백을 기준으로 숫자열로 받은것
#
# matrix = [(list(map(int, input()))) for _ in range(N)]
#
# visited = [[False] * M for _ in range(N)]
#
# ice_block_count = 0
#
# def dfs(matrix, n, m, visited):
#     visited[n][m] = True
#     for n in range(N):
#         for m in range(M):
#             if not visited[n][m]:
#                 dfs(matrix, n, m, visited)
#                 # 문제점: 연결된 블록 카운팅을 어떻게?
#
# dfs(matrix, 0, 0, visited)
#
# print(ice_block_count)
# # ---



# DFS / BFS 둘다 가능하구나, 그래프 탐색하는 알고리즘일 뿐, 한개만 성립하는게 아님



# # 2_X
#
# # DFS(depth first search) by recursive_function
#
# # 해당 문제에서 방문한 노드에 대한 정보는 matrix 그 자체의 정보를 이용 (0, 1)
#
# N, M = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(N)]
#
# ice_block_count = 0
#
# # 0 -> 방문값 False : 방문 아직 안함 / 1 -> 방문값 True : 방문 이미 했다
#
# # 범위 넘어가면 True return 해서 카운트 안되게
# def dfsR(x, y):
#     if (x < 0 or n <= x) or (y < 0 or m <= y):
#         return False
#     if matrix[x][y] == 0:
#         matrix[x][y] = 1
#         dfsR(x - 1, y)
#         dfsR(x, y - 1)
#         dfsR(x + 1, y)
#         dfsR(x, y + 1)
#         return True
#     return False
#
# for n in range(N):
#     for m in range(M):
#         if dfsR(n, m) == True:
#             ice_block_count += 1
#
# print(ice_block_count)
#
# # 핵심
# # dfsR 들어가서 수행 후 True 라면
# # ice_block_count 하나 올라감
# # dfsR의 내부 동작은 재귀로 연결부위를 방문처리하는 것
# # ---



# # 2-1_X
# # 헷갈려서 matrix를 방문 리스트로 변경
#
# N, M = map(int, input().split())
# visited = [(list(map(int, input()))) for _ in range(N)]
#
# ice_block_count = 0
#
# # 0 -> 방문값 False : 방문 아직 안함 / 1 -> 방문값 True : 방문 이미 했다
# for element in visited:
#     for index, value in enumerate(element):
#         if value == 0:
#             element[index] = False
#         else:
#             element[index] = True
#
# def dfsR(x, y, visited):
#     if (x < 0 or n < x) or (y < 0 or m < y):
#         return
#     visited[x][y] = True
#     dfsR(x - 1, y)
#     dfsR(x, y - 1)
#     dfsR(x + 1, y)
#     dfsR(x, y + 1)
#
# ice_block_count = 0
#
# for n in range(N):
#     for m in range(M):
#         if visited[n][m] == False:
#             dfsR(n, m, visited)
#             ice_block_count += 1
#
# print(ice_block_count)
# # 오히려 정리도 안됨
# # ---


# # 2-2-1_O
# # DFS
# # visited 활용 -> 탐색 후 맵의 변형없음
# from collections import defaultdict
#
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
# visited = defaultdict(bool)
#
# def dfsR(r, c):
#     # 탈출
#     if (r < 0 or R <= r) or (c < 0 or C <= c):
#         return
#     if (visited[(r, c)] == True) or matrix[r][c] == 1:
#         return
#     # recursive
#     visited[(r, c)] = True
#     dfsR(r - 1, c)
#     dfsR(r + 1, c)
#     dfsR(r, c - 1)
#     dfsR(r, c + 1)
#
# for i in range(R):
#     for j in range(C):
#         if matrix[i][j] == 0 and not visited[(i, j)]:
#             ice_block_count += 1
#             dfsR(i, j)
#
# print(ice_block_count)
# print(matrix)
# # ---


# # 2-2-2_O
# # DFS
# # visited 활용 안하고 / matrix의 0, 1로 방문 memo 대체하기 -> 탐색 후 맵의 변형 발생
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
#
# def dfsR(r, c):
#     # 탈출
#     if (r < 0 or R <= r) or (c < 0 or C <= c):
#         return
#     if matrix[r][c] == 1:
#         return
#     # recursive
#     matrix[r][c] = 1
#     dfsR(r - 1, c)
#     dfsR(r + 1, c)
#     dfsR(r, c - 1)
#     dfsR(r, c + 1)
#
# for i in range(R):
#     for j in range(C):
#         if matrix[i][j] == 0:
#             ice_block_count += 1
#             dfsR(i, j)
#
# print(ice_block_count)
# print(matrix)
# # ---


# # 3_X
# # BFS (breadth-first-search)
# from collections import deque
#
# N, M = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(N)]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append( (x, y) )
#     while queue:
#         x, y = queue.popleft()
#         matrix[x][y] = 1
#         if x - 1 >= 0 and matrix[x - 1][y] == 0 and (x - 1, y) not in queue:
#             queue.append((x - 1, y))
#         if x + 1 <= N and matrix[x + 1][y] == 0 and (x + 1, y) not in queue:
#             queue.append((x + 1, y))
#         if y - 1 >= 0 and matrix[x][y - 1] == 0 and (x, y - 1) not in queue:
#             queue.append((x, y - 1))
#         if y + 1 <= M and matrix[x][y + 1] == 0 and (x, y + 1) not in queue:
#             queue.append((x, y + 1))
#
# ice_block_count = 0
#
# for n in range(N):
#     for m in range(M):
#         if matrix[n][m] == 0:   # 방문완료한 곳은 건너 뛰는 조건식이 필요함 / 즉 방문에 대한 memo가 필요 / # 3-1-2에 해결
#             ice_block_count += 1
#             bfs(n, m)
#
# print(ice_block_count)
# # ---



# # 3-1_O
# 초안
# dx dy
# # BFS & visited 처리를 위한 defaultdict 사용
# from collections import deque, defaultdict
#
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
# visited = defaultdict(bool)
#
# for i in range(R):
#     for j in range(C):
#         # if matrix[i][j] == 0:
#         if matrix[i][j] == 0 and not visited[(i, j)]:
#             ice_block_count += 1
#
#             #BFS
#             queue = deque()
#             queue.append( (i, j) )
#             visited[(i, j)] = True
#             while queue:
#                 y, x = queue.popleft()  # i -> y , j -> x / 행계산: y축 이동 , 열계산: x축 이동
#                 for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:  # 상하좌우 이동
#                     y2 = y + dy
#                     x2 = x + dx
#
#                     # 이동값에서의 예외조건 / 밑 if 안보고 for로 넘어감(즉, 예외조건 만날 시 상하좌우 남은부분 탐색)
#                     if (y2 < 0 or R <= y2) or (x2 < 0 or C <= x2):  # 이동 위치가 맵 크기 밖
#                         continue
#                     if matrix[y2][x2] != 0: # 이동 위치의 값이 0이 아닌 값
#                         continue
#                     if visited[(y2, x2)]:   # 이동 위치를 방문했었음
#                         continue

#                     # 예외조건 통과하면
#                     visited[(y2, x2)] = True    # 방문처리
#                     queue.append( (y2, x2) )    # queue에 넣기
#
# print(ice_block_count)
# # ---



# # 3-1-1_O
# # BFS 함수 따로 빼기
# # dx dy로 이동
# from collections import deque, defaultdict
#
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
# visited = defaultdict(bool)
#
# def bfs(row, column):
#     queue = deque()
#     queue.append((row, column))
#     visited[(row, column)] = True
#     while queue:
#         y, x = queue.popleft()  # row -> y , column -> x / 행계산: y축 이동 , 열계산: x축 이동
#         for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우 이동
#             y2 = y + dy
#             x2 = x + dx
#
#             # 이동값에서의 예외조건 / 밑 if 안보고 for로 넘어감(즉, 예외조건 만날 시 상하좌우 남은부분 탐색)
#             if (y2 < 0 or R <= y2) or (x2 < 0 or C <= x2):  # 이동 위치가 맵 크기 밖
#                 continue
#             if matrix[y2][x2] != 0:  # 이동 위치의 값이 0이 아닌 값
#                 continue
#             if visited[(y2, x2)]:  # 이동 위치를 방문했었음
#                 continue
#
#             # 예외조건 통과하면
#             visited[(y2, x2)] = True  # 방문처리
#             queue.append((y2, x2))  # queue에 넣기
#
# for i in range(R):
#     for j in range(C):
#         if matrix[i][j] == 0 and not visited[(i, j)]:
#             ice_block_count += 1
#             bfs(i, j)
#
# print(ice_block_count)
# # ---
#
#
#
# # 3-1-2-1_O
# # BFS 함수 따로 빼기
# # list의 list element 이동
# from collections import deque, defaultdict
#
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
# visited = defaultdict(bool)
#
# def bfs(r, c):
#     queue = deque()
#     queue.append( (r, c) )
#     while queue:
#         r, c = queue.popleft()
#         visited[(r, c)] = True  # 큐에 한번 들어온 것은 pop 할때 방문처리됌
#
#         # 이동 위치: 맵 안쪽 / 방문하지 않음 / 큐에 있지 않다면 // 큐에 추가
#         if (r - 1 >= 0) and (matrix[r - 1][c] == 0) and (visited[(r - 1, c)] != True) and ((r - 1, c) not in queue):  # 상
#             queue.append((r - 1, c))
#         if (r + 1 < R) and (matrix[r + 1][c] == 0) and (visited[(r + 1, c)] != True) and ((r + 1, c) not in queue):   # 하
#             queue.append((r + 1, c))
#         if (c - 1 >= 0) and (matrix[r][c - 1] == 0) and (visited[(r, c - 1)] != True) and ((r, c - 1) not in queue):  # 좌
#             queue.append((r, c - 1))
#         if (c + 1 < C) and (matrix[r][c + 1] == 0) and (visited[(r, c + 1)] != True) and ((r, c + 1) not in queue):   # 우
#             queue.append((r, c + 1))
#
# for i in range(R):
#     for j in range(C):
#         if matrix[i][j] == 0 and not visited[(i, j)]:
#             ice_block_count += 1
#             bfs(i, j)
#
# print(ice_block_count)
# # ---


# # 3-1-2-2_O
# # BFS 함수 따로 빼기
# # list의 list element 이동
# # visited 활용 안하고 / matrix의 0, 1로 방문 memo 대체하기
# from collections import deque
#
# R, C = map(int, input().split())
# matrix = [(list(map(int, input()))) for _ in range(R)]
#
# ice_block_count = 0
#
# def bfs(r, c):
#     queue = deque()
#     queue.append( (r, c) )
#     while queue:
#         r, c = queue.popleft()
#         matrix[r][c] = 1    # 방문에 대한 처리를 1로 대신함 / 즉 0 인 노드만 들리기 위해
#
#         # 이동 위치: 맵 안쪽 / 값은 0 이고 /
#         if (r - 1 >= 0) and matrix[r - 1][c] == 0 and (r - 1, c) not in queue:  # 상
#             queue.append((r - 1, c))
#         if (r + 1 < R) and matrix[r + 1][c] == 0 and (r + 1, c) not in queue:   # 하
#             queue.append((r + 1, c))
#         if (c - 1 >= 0) and matrix[r][c - 1] == 0 and (r, c - 1) not in queue:  # 좌
#             queue.append((r, c - 1))
#         if (c + 1 < C) and matrix[r][c + 1] == 0 and (r, c + 1) not in queue:   # 우
#             queue.append((r, c + 1))
#
# for i in range(R):
#     for j in range(C):
#         if matrix[i][j] == 0:
#             ice_block_count += 1
#             bfs(i, j)
#
# print(ice_block_count)
# # ---