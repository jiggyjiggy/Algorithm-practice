# 전체 그래프에서 2개의 최소 신장 트리를 만들어야 한다(최소한의 비용으로)
# 크루스칼 알고리즘으로 최소 신장 트리를 찾고, 최소신장 트리를 구성하는 간선 중 가장 비용이 큰 간선 제거

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i]

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

result = 0
last = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)