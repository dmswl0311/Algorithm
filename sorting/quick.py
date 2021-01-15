import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for _ in range(n)]


def quick_sort(array, start, end):

    # 종료 조건
    if end-start <= 0:
        return

    pivot = start
    left = start+1
    right = end
    while (left <= right):
        while(left <= end and array[pivot] >= array[left]):
            left += 1
        while(right > start and array[pivot] <= array[right]):
            right -= 1
        # 큰값과 작은값의 범위가 겹치면 pivot과 작은값 swap
        if (left > right):
            array[pivot], array[right] = array[right], array[pivot]
        # 큰값, 작은값 찾아서 swap
        else:
            array[left], array[right] = array[right], array[left]
    # 분할
    quick_sort(array, start, right-1)  # right+1 이 아닌 이유는 피봇을 빼야하므로
    quick_sort(array, right+1, end)


quick_sort(array, 0, n-1)

for num in array:
    print(num, end=' ')
