n = int(input())
cnt = 0

for i in range(0, n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(k):
                cnt += 1
            elif '3' in str(j):
                cnt += 1
            elif '3' in str(i):
                cnt += 1

print(cnt)
