# 백준 18310

n = int(input())
array = sorted(list(map(int, input().split())))

if n % 2 == 0:
    mid = (n//2)-1
else:
    mid = (n//2)

print(array[mid])
