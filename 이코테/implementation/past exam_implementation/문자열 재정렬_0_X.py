data = input()

literal_target = []
nums = 0

for i in data:
    if ord("A") <= ord(i) <= ord("Z"):
        literal_target.append(ord(i))
    else:
        nums += int(i)

literal_target.sort()
string = "".join(chr(_) for _ in literal_target) + str(nums)

print(string)


###
# 입력예시
# AJKDLSI412K4JSJ9D
#
# 출력예시
# ADDIJJJKKLSS20

# 모범답안
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
###


