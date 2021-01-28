n, m, k = map(int, input().split())
array = sorted(list(map(int, input().split())), reverse=True)

result = 0
cnt = 0

while(cnt < m):
    for _ in range(k):
        result += array[0]
        cnt += 1
    result += array[1]
    cnt += 1

print(result)
