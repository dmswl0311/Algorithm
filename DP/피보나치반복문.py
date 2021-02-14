# DP
# 메모이제이션
# 반복문
# 보텀업

d = [0]*100
d[1] = 1
d[2] = 2
x = 99

for i in range(3, x+1):
    d[i] = d[i-1]+d[i-2]

print(d[x])
