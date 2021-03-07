import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        # 내림차순으로 정렬하고 싶다면 -value
        heapq.heappush(h, value)
    for i in range(len(h)):
        # 내림차순으로 정렬하고 싶다면 -heapq.heappop(h)
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
