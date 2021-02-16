# DP
# 실전문제 Q5

n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]
result = [10001]*(m+1)
result[0] = 0

for i in array:
    for j in range(i, m+1):
        result[j] = min(result[j], result[j-i]+1)


if result[m] == 10001:
    print(-1)
else:
    print(result[m])
