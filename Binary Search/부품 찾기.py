# 이진 탐색, 재귀
# 197p

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))
result = []


def binary_search(array, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)


for i in m_list:
    result.append(binary_search(n_list, 0, n-1, i))

for i in result:
    if i == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
