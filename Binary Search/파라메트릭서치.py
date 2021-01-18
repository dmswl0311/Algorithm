# 이코테 떡볶이 떡 만들기 문제 (201p)

import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)
result = 0

while(start <= end):
    mid = (start+end)//2
    total = 0
    for x in array:
        if x > mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
