# 기출
# 367p

n, x = map(int, input().split())
nlist = list(map(int, input().split()))
array = [0]*(nlist[-1]+1)
cnt = 0

for i in range(n):
    array[nlist[i]] += 1

for _ in range(array[x]):
    cnt += 1

print(cnt)
