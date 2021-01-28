n, m, k = map(int, input().split())
array = sorted(list(map(int, input().split())), reverse=True)

a = (array[0]*k)+array[1]

if m % (k+1) == 0:
    print((m//k)*a)
else:
    print(((m//k)*a)+(array[0]*(m % k)))
