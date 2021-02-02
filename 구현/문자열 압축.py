s = input().rstrip()
array = []
dap = []
cnt = 1
result = ''

# 예외처리
if len(s) == 1:
    print(1)
else:
    for i in range(1, (len(s)//2)+1):
        start = 0
        end = i
        for j in range(len(s)//i):
            array.append(s[start:end])
            start = end
            end = end+i
        if len(s) % i != 0:
            array.append(s[start:])
        same = 0
        for m in range(same+1, len(array)):
            if array[same] == array[m]:
                cnt += 1
                same = m
                if same >= len(array)-1:
                    result += str(cnt)+array[same]
                    cnt = 1
                    break
                else:
                    continue
            else:
                if cnt == 1:
                    result += array[same]
                else:
                    result += str(cnt)+array[same]
                cnt = 1
                same = m
            if same == (len(array)-1):
                result += array[same]

        dap.append(len(result))
        result = ''
        array = []

    print(min(dap))
