# 계수 정렬
# 197p

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))
array = [0]*(max(n_list)+1)

for i in range(len(n_list)):
    array[n_list[i]] += 1

for i in m_list:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
