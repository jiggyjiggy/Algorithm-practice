n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

array1.sort()

for i in array2:
    start = 0
    end = n
    while start <= end:
        mid1 = (start + end) // 2
        if array1[mid1] > i:
            end = mid1 - 1
        elif array1[mid1] < i:
            start = mid1 + 1
        elif array1[mid1] == i:
            print('yes', end=' ')
            break
    else:
        print('no', end=' ')


