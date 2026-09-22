# N x M 직사각형에 1부터 순서대로 증가시키며 달팽이 모양으로 채우는 프로그램

# 달팽이 모양:
    # 반시계 방향

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

# 입력
N, M = map(int, input().strip().split())

# 격자
arr = [[0] * M for _ in range(N)]

# didj, dir
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
dir_num = 1

# 초기화
ci, cj = 0, 0
arr[ci][cj] = 1

for i in range(2, N*M+1):
    ni, nj = ci + di[dir_num], cj + dj[dir_num]

    if not in_range(ni, nj) or arr[ni][nj] != 0:
        dir_num = (dir_num - 1 + 4) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]
    
    arr[ni][nj] = i
    ci, cj = ni, nj

for row in arr:
    print(*row)
