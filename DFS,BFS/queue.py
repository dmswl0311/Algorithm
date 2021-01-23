from collections import deque

queue = deque()

queue.append(2)
queue.append(1)
queue.append(6)
queue.popleft()  # 그냥 pop하면 안됨

print(queue)
print(list(queue))
