n, target = map(int, input().split())
array = list(map(int, input().split()))


def binary_search(array, target, start, end):

    if start > end:
        return None

    mid = (end+start)//2

    if (array[mid] > target):
        return binary_search(array, target, start, mid-1)
    elif (array[mid] == target):
        return mid
    else:
        return binary_search(array, target, mid+1, end)


result = binary_search(array, target, 0, n-1)

if (result == None):
    print(0)
else:
    print(result+1)
