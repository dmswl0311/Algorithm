# dijkstra
# 백준 18352번

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(x)

if k not in distance:
    print(-1)
else:
    for i in range(1, n+1):
        if distance[i] == k:
            result.append(i)
    result.sort
    for j in result:
        print(j)
