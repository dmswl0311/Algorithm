import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수
n = int(input())
# 주어지는 간선의 개수
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 간선의 길이는 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

# 그래프에 간선 길이 입력 받음
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x][y] = z

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] != INF:
            print(graph[i][j], end=" ")
        else:
            print("INFINITY", end=" ")
    print(" ")
