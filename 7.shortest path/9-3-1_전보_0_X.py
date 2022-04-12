import heapq
n, m, c = map(int, input().split())

graph = []
for i in range(m):
    x, y, z = map(int, input().split())
    graph.append((x, y, z))

INF = int(1e9)

time = [0] * n

def dijkstra(start, end):

    q = []
    heapq.heappush(q, (start, 0, 0))
    time[start] = 0
    while q:
        start, now, t = heapq.heappop(q)
        if time[now] > t:
            continue

        # for i in graph[now]:
        for idx, value in enumerate(graph):
            tttt = time[idx-1] + t
            if tttt > time[idx]:
                time[idx] = tttt
                if graph[0] == now:
                    heapq.heappush(q, graph)

dijkstra(start=0, end=c)
