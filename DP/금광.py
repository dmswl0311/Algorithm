# DP

t = int(input())
result = []

for _ in range(t):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    array = [[0]*m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            array[i][j] = num_list[cnt]
            cnt += 1
    print(array)
    dx = [-1, 0, 1]
    dy = [1, 1, 1]

    next = 0
    x = 0
    y = 0
    sum = 0

    for i in range(n-1):
        if array[i][0] < array[i+1][0]:
            x = i+1
        else:
            continue

    sum += array[x][y]
    print(sum)

    for _ in range(m-1):
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < n and ny < m:
                if next < array[nx][ny]:
                    next = array[nx][ny]
        x = nx
        y = ny
        sum += next
        print(sum)
        next = 0
    result.append(sum)

for i in result:
    print(i)
