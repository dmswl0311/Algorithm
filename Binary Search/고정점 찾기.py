# 기출
# 368p

n = int(input())
array = list(map(int, input().split()))


def search(start, end, array):
    if start > end:
        return None
    mid = (start+end)//2

    if mid == array[mid]:
        return mid
    elif mid > array[mid]:
        return search(mid+1, end, array)
    else:
        return search(start, mid-1, array)


result = search(0, n-1, array)
if result == None:
    print(-1)
else:
    print(result)
