n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))
# graph: [[0, 0, 1], [0, 1, 0], [1, 0, 1]]

def dfs(x, y):
    if (x < 0 or n <= x) or (y < 0 or m <= y):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)   # 상
        dfs(x + 1, y)   # 하
        dfs(x, y - 1)   # 좌
        dfs(x, y + 1)   # 우
        return True
    return False

result = 0

for row in range(n):
    for column in range(m):
        if dfs(row, column) == True:
            result += 1

print(result)