# 격자: N x N

# 색칠
    # M번
    # 한 번에 한 칸
    # 색칠 직후 해당 칸이 '편안한 상태'에 놓여있는지 확인

# 편안한 상태
    # 인접한(상하좌우) 칸 중 색칠되어있는 칸이 정확히 3개인 경우
    # + 범위 내

# 색칠할 칸이 주어질 때 마다 색칠 직후, 편안한 상태에 있는지 알아내는 프로그램

import sys
input = sys.stdin.readline
answer = 0

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

# 입력
N, M = map(int, input().strip().split())
colors = [list(map(int, input().strip().split())) for _ in range(M)]

# 격자
arr = [[0] * N for _ in range(N)]

# 색칠
for i, j in colors:
    ci, cj = i-1, j-1 # 주어진 좌표는 1~N까지라서 -1
    count = 0 # 인접칸 중 색칠된 칸 카운팅하는 변수
    # 색칠
    arr[ci][cj] = 1

    # 편안한 상태 확인
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj

        if in_range(ni, nj) and arr[ni][nj]:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)