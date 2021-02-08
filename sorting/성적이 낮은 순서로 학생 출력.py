n = int(input())
array = []

for i in range(n):
    a, b = map(str, input().split())
    array.append((a, int(b)))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], end=' ')
