0시부터 N시 59분 59초까지의 모든 시각중 3이 포함되는 모든 경우의 수
입력
N
출력
갯수

방법 1 datetime library
N입력에 대해  저장
00시 00분 00초 ~ N시 59분 59초
시:분:초 를 :기준으로 나누고, # <- 필요 없는 과정인듯
시분초의 각자리 를 문자로 변환
루프돌리면서 3이 1개 이상 존재하면 카운팅

N = int(input())

import datetime
target = datetime.time(N,59,59)

def time_matching(i):
  return hour[i] == '3' or minute[i] == '3' or second[i] == '3'

count = 0
# 시각 순회
for H in range(target.hour):
  hour = str(H)
  for M in range(target.minute):
    minute = str(M)
    for S in range(target.second):
      second = str(S)

      if H >= 10 and M >= 10 and S >= 10:           # 2^3 = 8번의 if문 만들어야한다...
        if time_matching(0) or time_matching(1):
          count += 1
      elif
        if time_matching(0):
          count += 1
print(count)



방법 2 근데 실시간이 필요한게 아님 ->



