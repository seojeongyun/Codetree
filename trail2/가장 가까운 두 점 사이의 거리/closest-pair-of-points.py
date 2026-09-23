# 2차원 평면 위에 점 N개
    # i번째 점 위치를 xi, yi
    # 서로 다른 두 점 i, j의 거리의 제곱은 (xi-xj)^2 + (yi-yj)^2로 정의
# 두 점 사이의 거리의 제곱의 최솟값 구하기

import sys
input = sys.stdin.readline
answer = sys.maxsize

def dist(point1:tuple, point2:tuple):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

N = int(input().strip())
coords = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        v = dist(coords[i], coords[j])
        answer = min(answer, v)

print(answer)
