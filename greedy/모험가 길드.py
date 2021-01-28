# 유형별 기출 - 그리디
# 311p

n = int(input())
num = sorted(list(map(int, input().split())))
cnt = 0
result = 0

for i in num:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)
