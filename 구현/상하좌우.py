n = int(input())
num_list = list(map(str, input().split()))

next_x = 0
next_y = 0

for i in num_list:
    x = next_x
    y = next_y

    if i == "R":
        next_y = y+1
    elif i == "L":
        next_y = y-1
    elif i == "U":
        next_x = x-1
    elif i == "D":
        next_x = x+1
    if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n:
        next_x = x
        next_y = y

print(next_x+1, next_y+1)
