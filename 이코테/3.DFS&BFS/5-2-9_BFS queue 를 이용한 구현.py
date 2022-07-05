# queue 사용을 위해 deque import
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 list 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],  # 노드1은 노드2, 노드3, 노드8과 연결돼있다
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 list로 표현(1차원 리스트)
visited = [False] * 9   # 초기값은 (아직 어떤 노드도 방문하지 않았기에) False element로 list 생성 / 저장할 노드 갯수만큼 곱한 것
# 출력시 : [False, False, False, False, False, False, False, False, False]

# 정의된 bFS 함수 호출
bfs(graph, 1, visited)
