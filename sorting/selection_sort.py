import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]

for i in range(n):
    least = i
    for j in range(i+1, n):
        if(array[least] > array[j]):
            least = j
    if(least != i):
        array[i], array[least] = array[least], array[i]

for num in array:
    print(num, end=' ')
