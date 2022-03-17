def find_parent(parent, x):
    # if not root node, return recursive func.
    # 본인 인덱스가 본인 값이 아니면 재귀
    if parent[x] != x:
        # 재귀에서 특이점은 2번째 argument가 함수 parameter에선 x로 받음, 즉 바뀐 노드번호를 통해 parent값을 조회하고, root노드까지 조회하는 것
        return find_parent(parent, parent[x])
    return x

# 합집합
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# main
# v: node, e: directed edge
v, e = map(int, input().split())
parent = [0] * (v + 1) 

for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end=" ")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')