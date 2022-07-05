# <기성> [X] : 로직 완전 잘못된 방향; 지금 로직은 두개만 뽑아서 더하는 연산
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 1

if data[0] != 1:
    print(result)
else:
    target = []
    target.append(result)
    for i in data:
        for j in data[1:]:
            target.append(i+j)
    target.sort()

    for idx, value in enumerate(target):
        if idx == len(target) - 1:
            result = value + 1
            break

        if target[idx + 1] - target[idx] > 1:
            result = value + 1
            break

    print(result)


###
# 입력예시
# 5
# 3 2 1 1 9
#
# 출력예시
# 8

# 모범답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
###