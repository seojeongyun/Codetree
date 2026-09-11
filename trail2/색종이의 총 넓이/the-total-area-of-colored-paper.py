# 격자 위에 색종이(8X8)가 N장 놓여
# 색종이 각 좌측하단의 꼭지점이 주어졌을 때 모든 색종이가 붙여진 이후 총 넓이를 구해라.

import sys
input = sys.stdin.readline

N = int(input().strip())
coords = [list(map(int, input().strip().split())) for _ in range(N)]
arr = [[0] * 201 for _ in range(201)]
answer = 0

for x, y in coords:
    for i in range(y, y+8):
        for j in range(x, x+8):
            arr[i][j] = 1


for i in range(201):
    for j in range(201):
        if arr[i][j] > 0:
            answer += 1

print(answer)


