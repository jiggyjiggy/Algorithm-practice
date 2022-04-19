# N, M, K = input().split() 이렇게 받으면 string이므로 int로 받아야하기에 map으로 int를 씌워서 받
N, M, K = map(int, input().split())   # N:n개의 자연수, M:총 m번 더함, K:같은수 최대 k번 연속 덧셈가능
data = list(map(int, input().split()))  # 큰 수 뽑기위한 방법으로 -> sort() / sort() 쓰기위해 list 객체로 전환
data.sort()

first_big = data[N - 1] # 오름차순이기에 마지막이 제일큼
second_big = data[N - 2]


# 큰 수 연속돌리고 그다음 큰 수 끠워서 더함
result = 0  # 연산결과 담을 곳

while M > 0:
    for _ in range(K):
        result += first_big
        M -= 1
        if M <= 0:
          break
    if M <= 0:
        break
    result += second_big
    M -= 1

# 다만 이런식이면 while loop 실행중 M의 값이 음이 나와도 돌아가기 때문에 오답
# 따라서 loop 중간에 M의 값을 확인 하는 로직이 필요
# if를 통해 탈출조건 추가,
# 탈출 조건시 second_big이 더해지기 전에 탈출해야하므로
# 탈출 조건을 유닛 위쪽으로 배치시킴

print(result)