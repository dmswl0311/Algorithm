# DP

n = int(input())
d = list(map(int, input().split()))
array = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    for j in range(2, n-i):
        if array[i][j] == 0:
            array[i][j] = d[i]+d[i+j]

print(max(max(array)))
