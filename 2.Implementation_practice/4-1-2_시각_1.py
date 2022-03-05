h = int(input())

count = 0

for i in range(h+1):    # 시 분 초를 변수 저장하는게 아니라 반복문 속에서 반복문의 값 자체를 문자열로 저장
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) +str(k):  # 합친 문자열에서 in operator로 탐색
                count += 1

print(count)