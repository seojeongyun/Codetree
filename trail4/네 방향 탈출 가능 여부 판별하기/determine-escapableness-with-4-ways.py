# 격자: N x M
# 이동
    # Start = 0, 0
    # End = N-1, M-1
    # 상하좌우에 인접 칸으로만 가능
    # 뱀이 있는 칸으로 이동 불가능

import sys
from collections import deque
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs(start):
    dq = deque([start])

    while dq:
        ci, cj = dq.popleft()
        # 종료 조건
        if (ci, cj) == (N-1, M-1):
            return 1

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di , cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj]:
                dq.append((ni, nj))
                v[ni][nj] = 1

    return 0

# 입력
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# BFS
v = [[0] * M for _ in range(N)]
start = (0, 0)
print(bfs(start))

