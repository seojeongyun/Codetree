# 2차원 평면 위에 N개의 점
# 그 중 3개를 골라 삼각형을 만든다
    # 한 변은 x축에 평행, 다른 변은 y축에 평행
# 삼각형 최대 넓이에 2를 곱한 값을 구하시오 = 직사각형 넓이
# 그런 삼각형이 없다면 0을 출력

import sys
input = sys.stdin.readline
answer = -sys.maxsize

N = int(input().strip())
coords = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # 서로 다른 i, j, k를 뽑고
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            x3, y3 = coords[k]

            # 한 변은 x축에 평행하고 다른 변은 y축에 평행하는 삼각형
            if (x1 == x2 and (y1 == y3 or y2 == y3)) or (x2 == x3 and (y2 == y1 or y3 == y1)) or (x1 == x3 and (y1 == y2 or y3 == y2)):
                S = abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))

                answer = max(answer, S)

if answer != -sys.maxsize:
    print(answer)

else:
    print(0)