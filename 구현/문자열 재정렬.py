s = input()
alpha = []
n = []

for i in s:
    if 65 <= ord(i) <= 90:
        alpha.append(str(i))
    else:
        n.append(int(i))

alpha.sort()

for i in alpha:
    print(i, end='')

print(sum(n))
