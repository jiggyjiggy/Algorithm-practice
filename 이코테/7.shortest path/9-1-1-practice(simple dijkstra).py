# input
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# output
# 0
# 2
# 3
# 1
# 2
# 4

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

visited = [False] * (n + 1)

INF = int(1e9)
distance = [INF] * (n + 1)

def simple_dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):

