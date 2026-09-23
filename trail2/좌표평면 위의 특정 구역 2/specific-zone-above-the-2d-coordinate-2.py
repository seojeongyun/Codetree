# 좌표평면 위에 점 N개
# N개의 점 중 하나를 제외했을 때, 남은 점들을 모두 포함하는 각 변이 좌표축에 평행한 직사각형의 넓이를 최소로
    # 상하좌우에 대해 가장 바깥 쪽에 위치한 점들 구하기

# 모두 x가 같거나 y가 같은 경우 넓이가 0이 될 수도 있다.

import sys
input = sys.stdin.readline
answer = sys.maxsize

N = int(input().strip())
coords = [list(map(int, input().strip().split())) for _ in range(N)]

# i: 제외할 번호, j: 선택할 번호
# i == j 면 continue
for i in range(N):
    x_min, x_max = sys.maxsize, -sys.maxsize
    y_min, y_max = sys.maxsize, -sys.maxsize
    for j in range(N):
        if i == j: continue

        # 직사각형 찾기
        # x최소, y최대, x최대, y최소 구하고 x최대-최소 * y최대-최소
        x_min = min(x_min, coords[j][0])
        x_max = max(x_max, coords[j][0])
        #
        y_min = min(y_min, coords[j][1])
        y_max = max(y_max, coords[j][1])
    
    # 직사각형 넓이 구하기
    answer = min(answer, (x_max-x_min) * (y_max-y_min))

print(answer)
