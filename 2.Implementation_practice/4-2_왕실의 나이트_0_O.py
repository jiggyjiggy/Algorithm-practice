# a1(초기좌표) 입력받고 (우선 str으로)
# 영어, 숫자 쪼개기
# 영어는 숫자로 바꾸기, a 기준점 (ASCII, 1로 좌표변환)
#
# 이동 계획 저장해두기
#
# 이동 계획적용할 임시변수 저장 & 가능여부 판별
# 가능하면 이동 좌표 반환

start = input()
start_point = [ord(start[0])-96, int(start[1])]

plan = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

count = 0

for i in plan:
    x_total_end_point = start_point[0] + i[0]
    y_total_end_point = start_point[1] + i[1]
    dx = x_total_end_point
    dy = y_total_end_point
    if (0 < dx & dx <= 8) & (0 < dy & dy <= 8):
        # x = dx
        # y = dy
        count += 1

print(count)