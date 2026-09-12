# 좌표평면 위에 N개의 직사각형이 주어짐
    # 주어진 순서대로 하나씩 칠해짐
        # 첫 번째는 빨간색
        # 두 번째는 파란색
        # 세 번째는 빨간색
        # ... 빨,파가 번갈아 등장
    # 이미 칠해져 있던 색 위에 덧칠된다.
# N개를 모두 칠한 뒤 파란 영역의 총 넓이를 구해라.

import sys
input = sys.stdin.readline
answer = 0

N = int(input().strip())
# (x1, y1, x2, y2): 1은 좌하단, 2는 우상단
rect_coords = [list(map(int, input().strip().split())) for _ in range(N)]

# -100부터 100까지이므로, 201
MAX_SIZE = 201
OFFSET = 100

arr = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]

for idx, (x1, y1, x2, y2) in enumerate(rect_coords):
    x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    if idx % 2 == 0: # 빨
        rect_value = 1
    else: # 파
        rect_value = 2

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = rect_value


for i in range(MAX_SIZE):
    for j in range(MAX_SIZE):
        if arr[i][j] == 2:
            answer += 1

print(answer)