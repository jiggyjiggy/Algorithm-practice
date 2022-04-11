import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = []
for i in range(m):
    a,b = (map(int, input().split()))
    graph.append((a,b))

x, k = map(int, input().split())

distance = [INF] * (n+1)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    if distance[end] != INF:
        return distance[end]
    else:
        return -1

result = dijkstra(start=0 ,end=x-1) + dijkstra(start=x-1, end=k-1)
print(result)