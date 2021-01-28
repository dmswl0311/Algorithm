n, m = map(int, input().split())

array = [[0]*m for _ in range(n)]

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(m):
        array[i][j] = num[j]
    num = 0
result = []
for i in range(n):
    result.append(min(array[i][:]))

print(max(result))
