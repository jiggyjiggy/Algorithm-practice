data = input()

length = len(data)

left_target = 0
right_target = 0

for left in data[:(length // 2)]:
    left_target += int(left)
for right in data[(length // 2):]:
    right_target += int(right)

if left_target == right_target:
    print("LUCKY")
else:
    print("READY")


###
# 입력예시
# 123402
#
# 출력예시
# LUCKY

# 모범답안
n = input()
length = len(n)
summary = 0

for i in range(length // 2):
    summary += int(n[i])

for i in range(length // 2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
###