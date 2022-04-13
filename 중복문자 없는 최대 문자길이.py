# 중복문자 없는 최대 문자길이

s = "pwwkew"
target = []

for i in range(len(s)):
    for j in range(i,len(s)):
        # if len(set(s[i:j])) != len(set(s[i+1:j+1])):


            # print(s[i:j+1])
            # print(set(s[i:j + 1]))
            # print(len(set(s[i:j + 1])))
            # print(s[i+1:j+1])