# int(input())
# input()자체는 받은 값을 문자열로 저장함
# 1개 받음
n = int(input())


# list(map(int, input().split()))
# input()으로 입력받은 문자열을
# split()을 이용해 공백으로 받고
# int로 정수화 시키고
# map object로 결과 반환
# list로 저장

# +) map 함수는 원본 list를 변경하지 않고 새 list를 생성
# +) map 함수는 map type으로 결과를 리턴한다
# +) range()처럼 하나씩만 꺼내서 보여주기때문에 한번에 보여주기 위해서는 list나 tuple로 변환하는 것
# +) 하나씩 보여주려면 next()로 꺼낸다
# +) map object 자제는 indexing이 불가능

# 바로 list object에 assign
data = list(map(int, input().split()))
# 출력도 list로 나옴

# map 자체로 받는다면 입력값 갯수만큼 변수 지정해야함
data1, data2, data3, ... = map(int, input().split())


# 입력값이
# 1줄에 1개: input
# 1줄에 여러개: map
# 여러줄에 1개: input 반복
# 여러줄에 여러개: map 반복


# 입력이 많다면 input() 함수는 동작속도가 느려서 시간초과 가능성이 있음
# 파이썬의 sys 라이브러리에 정의되어있는 sys.stdin.readline() 사용
# readline()으로 입력하면 입력후 엔터를 치면 엔터가 줄바꿈 기호(공백 문자)로 입력되는데,
# 이 공백 문자를 제거하고자 rstrip() 함수를 쓴다

import sys
data = sys.stdin.readline().strip() # 입력값은 str type 이다

