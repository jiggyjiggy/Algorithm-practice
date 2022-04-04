n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

array1.sort()

def binary_search(array1, i, end, start):
    mid1 = (start + end) // 2
    if start <= end:
        if array1[mid1] > i:
            return binary_search(array1, i, mid1 - 1, start)
        elif array1[mid1] < i:
            return binary_search(array1, i, end, mid1 + 1)
        elif array1[mid1] == i:
            return print("yes", end=' ')
    else:
        return print("no", end=' ')


for i in array2:
    binary_search(array1, i, end=n, start=0)