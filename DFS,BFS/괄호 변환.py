# 2020 카카오 신입 공채 1차

w = str(input())


def right(p):
    list = []
    list.append(p[0])
    for i in p[1:]:
        if len(list) == 0:
            list.append(i)
            continue
        if list[-1] != i:
            if list[-1] == "(" and i == ")":
                list.pop()
            else:
                list.append(i)
        else:
            list.append(i)


right(w)

if len(list) == 0:
    print(w)
else:  # 올바른 아니면
    if w == " ":
        return print(w)
    else:
        w.split
