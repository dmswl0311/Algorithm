import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(1, n):
    for j in range(i, 0, -1):
        if (array[j] < array[j-1]):
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for num in array:
    print(num, end=' ')
