# 실전문제
# 344p
from sys import stdin

n, k = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
s, x, y = map(int, stdin.readline().split())


def v():
    cnt = 1
    while(cnt <= k):
        for i in range(n):
            for j in range(n):
                if graph[i][j] == cnt:
                    for c in range(4):
                        ni = i+dx[c]
                        nj = j+dy[c]
                        if ni >= 0 and nj >= 0 and ni < n and nj < n:
                            if graph[ni][nj] == 0:
                                graph[ni][nj] = cnt
                        else:
                            continue
                    cnt += 1


for _ in range(s):
    v()

print(graph[x-1][y-1])
