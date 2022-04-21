def top_k(nums, k):
  list = []
  count_list = []
  result = []
  real = []
  for i in range(len(nums)):
    list.append(nums.count(nums[i]))
  for j in range(len(list)):
    if list[j] not in count_list:
      count_list.append(list[j])
  for n in range(k):
    count_list.sort(reverse=True)
    result.append(count_list[n])
  for m in range(len(result)):
    real.append(nums[list.index(result[m])])
  return real