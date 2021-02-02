n, m = map(int, input().split())
x, y, flag = map(int, input().split())
array = [[0]*m for _ in range(n)]
visit = [[0]*m for _ in range(n)]

for i in range(n):
    num_list = list(map(int, input().split()))
    for j in range(m):
        array[i][j] = num_list[j]
    num_list = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate():
    global flag
    flag -= 1
    if flag == -1:
        flag = 3


visit[x][y] = 1
r = 0
cnt = 1

while(True):
    rotate()
    nx = x+dx[flag]
    ny = y+dy[flag]

    if visit[nx][ny] == 0 and array[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        r = 0
        cnt += 1
        continue
    else:
        r += 1
    if r == 4:
        nx = x-dx[flag]
        ny = y-dy[flag]
        if(array[nx][ny] == 0):
            visit[nx][ny] = 1
            x = nx
            y = ny
        else:
            break
        r = 0

print(cnt, visit)
