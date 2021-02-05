# 실전문제
# 341p
# 삼성sw역테

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
test = [[0]*m for _ in range(n)]

# 바이러스 퍼지는 함수
# 안전지대 갯수 세는 함수
# 울타리 세우고, 바이러스 퍼지는 함수, 안전지대 갯수 함수 통합하는 함수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if test[nx][ny] == 0:
                test[nx][ny] = 2
                virus(nx, ny)


result = 0


def safe():
    score = 0
    for i in range(n):
        for j in range(m):
            if test[i][j] == 0:
                score += 1

    return score


def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                test[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if test[i][j] == 2:
                    virus(i, j)
        result = max(result, safe())
        return result

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(result)
