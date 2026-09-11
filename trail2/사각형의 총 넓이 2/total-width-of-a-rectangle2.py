# N개의 직사각형이 주어진다.
# 직사각형들이 덮는 영역 전체의 넓이를 구하시오.
    # 두 개 이상의 직사각형이 겹치는 부분은 한 번만 센다.
import sys
input = sys.stdin.readline

N = int(input().strip())

# [x1, y1, x2, y2] : x1 y1이 좌하단, x2 y2가 우상단
xy_lst = [list(map(int, input().strip().split())) for _ in range(N)]

arr = [[0] * 201 for _ in range(201)]
answer = 0
min_val = sys.maxsize
OFFSET = 100
# for x1, y1, x2, y2 in xy_lst:
#     # 음수 처리
#     if x1 < 0 or y1 < 0 or x2 < 0 or y2 < 0:
#         min_val = min(min_val, min(x1, y1, x2, y2))

for x1, y1, x2, y2 in xy_lst:
    x1 = x1 - OFFSET
    x2 = x2 - OFFSET
    y1 = y1 - OFFSET
    y2 = y2 - OFFSET
    
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] += 1


for i in range(201):
    for j in range(201):
        if arr[i][j] > 0:
            answer += 1

print(answer)