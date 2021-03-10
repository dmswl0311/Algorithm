# 실전문제 3 전보
# 262p

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance[start] = 0

    while h:
        dist, now = heapq.heappop(h)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))


dijkstra(c)
cnt = 0
max_time = 0
for i in distance:
    if i != INF:
        cnt += 1
        if i > max_time:
            max_time = i

print(cnt-1, max_time)
