n = int(input())    # N 입력받기
x, y = 1, 1 # 초기좌표 설정
plans = input().split()       # 이동 계획 입력받기

dx = [0, 0, -1, 1]  # U: row - 1, D: row + 1
dy = [-1, 1, 0, 0]  # L: column - 1, R: column + 1
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    print(f"{plan} 받음")
    for i in range(len(move_types)):    # movetype 저장한 list의 element와 비교하기위해 loop 생성
        print(f"L:0, R:1, U:2, D:3, 탐색 index:{i}")
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(f"{plan}: index {i}")
            print("우선 nx, ny에 저장", nx, ny)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        print(f'{plan}에 의한 이동 위치는 지도밖으로 나감')
        print('nx, ny는 변경사항 무시함')
        continue
    x, y = nx, ny
    print(f"{plan}에 의한 이동 위치는 지도밖으로 안나갔음")
    print('nx, ny는 변경사항 저장')
print(x, y)


# 시간 복잡도 = O(N)
# 연산횟수는 이동횟수에 비례