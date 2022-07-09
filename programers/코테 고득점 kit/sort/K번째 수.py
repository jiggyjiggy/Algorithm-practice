###
def solution(array, commands):

    answer = []
    for command in commands:
      start = command[0] - 1
      end = command[1]
      select = command[2] - 1
      slice_arr = array[start:end]
      slice_arr.sort()
      answer.append(slice_arr[select])

    return answer
###

###
# 다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
###