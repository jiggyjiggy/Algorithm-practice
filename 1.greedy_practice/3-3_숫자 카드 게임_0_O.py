N, M = map(int, input().split())

data = [[] for _ in range(N)]
smallest_nums = []

for n in range(N):
    data[n] = list(map(int, input().split()))
    data[n].sort()
    small_nums = data[n][0]
    smallest_nums.append(small_nums)
# for loop / sort() : O(NlogN) / append() : O(1)
# TimeComplexity: O(N^2logN)

smallest_nums.sort()

print(smallest_nums[-1])

# min(), max() : O(N)
# sort()는 아껴쓰자..!

# N, M = map(int, input().split())
#
# data = [[] for _ in range(N)]
#
# for n in range(N):
#     data[n] = list(map(int, input().split()))
#     data[n].sort()
#
# smallest_nums = []
# for n in range(N):
#     small_nums = data[n][0]
#     smallest_nums.append(small_nums)
#
# smallest_nums.sort()
#
# print(smallest_nums[-1])

