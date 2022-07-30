def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result


###
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 입력예시
# # key
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# # lock
# [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 출력예시
# true

# 모범답안
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False
###


###
# 프로그래머스 주목할만한 풀이
# 풀이자: - , guitar-etc , smi1230
def solution(key, lock):
    N = len(lock)
    v, vac = vacant(lock)
    if not vac: return True
    vac = vac[0]
    find = False
    for key in rotate(key):
        for i in range(len(key)):
            cnt = 0
            rr, cc = vac[0]-key[i][0], vac[1]-key[i][1]
            print(rr, cc)
            for j in range(i, len(key)):
                r, c = key[j]
                r, c = r+rr, c+cc
                if not (0 <= r < N and 0 <= c < N): continue
                if lock[r][c] == 1: break
                cnt += 1
            if cnt == v:
                find = True
                break
        if find: break
    if find: return True
    return False


def vacant(lock):
    N = len(lock)
    vac = []
    v = 0
    for r in range(N):
        for c in range(N):
            if lock[r][c] == 0:
                vac.append((r, c))
                v += 1
    return v, vac


def rotate(key):
    M = len(key)
    key1 = [(r, c) for r in range(M) for c in range(M) if key[r][c] == 1]
    key2 = [(M-r-1, c) for c, r in key1]
    key3 = [(r, M-c-1) for c, r in key1]
    key4 = [(M-r-1, M-c-1) for r, c in key1]

    key1 = quick_sort(key1)
    key2 = quick_sort(key2)
    key3 = quick_sort(key3)
    key4 = quick_sort(key4)
    print(key1, key2, key3, key4)

    return key1, key2, key3, key4


def quick_sort(arr):
    if not arr: return []
    pivot = arr[len(arr)//2]
    lesser, equal, greater = [], [pivot], []

    for pos in arr:
        if pos[0] < pivot[0]:
            lesser.append(pos)
        elif pos[0] > pivot[0]:
            greater.append(pos)
        else:
            if pos[1] < pivot[1]:
                lesser.append(pos)
            elif pos[1] > pivot[1]:
                greater.append(pos)

    return quick_sort(lesser) + equal + quick_sort(greater)
###


