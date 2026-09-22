# 격자: N x M
    # 1부터 순서대로 증가시키며 달팽이 모양(시계 방향)으로 값을 채우는 코드 작성
    # 시작 지점: 왼쪽 위 모서리

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

# 입력
N, M = map(int, input().strip().split())

# 격자 생성
arr = [[0] * M for _ in range(N)]

# didj, dir
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
ci, cj, dir = 0, 0, 0

# arr, v 초기값 설정
arr[ci][cj] = 1

# 값 생성
for i in range(2, N*M+1):
    ni, nj = ci + di[dir], cj + dj[dir]

    if not in_range(ni, nj) or arr[ni][nj]:
        dir = (dir+1) % 4

    ci, cj = ci + di[dir], cj + dj[dir]
    arr[ci][cj] = i

for row in arr:
    print(*row)