# 격자: N x M
    # 시계방향 달팽이 모양으로 'A' to 'Z'까지 채우기
    # 'Z' 다음은 다시 'A'

import sys
input = sys.stdin.readline
alpha_lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

# 입력
N, M = map(int, input().strip().split())

# 격자
arr = [[0] * M for _ in range(N)]

# didj, dir
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
dir_num = 0

# 초기화
ci, cj = 0, 0
arr[ci][cj] = 'A'

for i in range(1, N*M):
    ni, nj = ci + di[dir_num], cj + dj[dir_num]

    if not in_range(ni, nj) or arr[ni][nj] != 0:
        dir_num = (dir_num + 1) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]

    arr[ni][nj] = alpha_lst[i%len(alpha_lst)]
    ci, cj = ni, nj

for row in arr:
    print(*row)