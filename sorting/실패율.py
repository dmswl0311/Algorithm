# 정렬
# 2019 카카오 신입공채 1차

n = int(input())
stages = list(map(int, input().split()))
array = [0]*(n+2)
ratio = []
result = []

for i in range(len(stages)):
    array[stages[i]] += 1

human = len(stages)

for i in range(1, len(array)-1):
    if array[i] == 0:
        ratio.append((0, i))
        continue
    else:
        ratio.append((array[i]/human, i))
        human = human-array[i]

ratio.sort(key=lambda x: -x[0])

for i in ratio:
    result.append(i[1])
