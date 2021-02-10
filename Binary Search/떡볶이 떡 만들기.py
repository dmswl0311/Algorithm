n, m = map(int, input().split())
dduck = sorted(list(map(int, input().split())), reverse=True)
result = dduck[0]
sum = 0

while(sum != m):
    sum = 0
    for i in dduck:
        if i >= result:
            sum += i-result
        else:
            break
    result -= 1

print(result+1)
