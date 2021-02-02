n = input()
x = int(n[1])
y = int(ord(n[0])-96)

dx = [1, -1, -1, 1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

cnt = 0

for i in range(8):
    nx = x+dx[i]
    ny = y+dy[i]

    if nx <= 0 or nx >= 9 or ny <= 0 or ny >= 9:
        continue
    else:
        cnt += 1

print(cnt)
