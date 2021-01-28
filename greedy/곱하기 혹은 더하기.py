# 유형별 기출 - 그리디
# 312p

s = input()
result = int(s[0])

for i in range(1, len(s)):
    if result and int(s[i]) > 1:
        result *= int(s[i])
    else:
        result += int(s[i])

print(result)
