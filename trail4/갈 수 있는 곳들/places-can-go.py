# 격자: N x N
    # 0, 1로만 구성

# K개의 시작점으로부터 상하좌우로 이동
# 도달 가능한 서로 다른 칸의 수를 구하는 프로그램

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
start = [list(map(int, input().strip().split())) for _ in range(K)]

answer = 0

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(i, j, v):
    dq = deque([(i, j)])
    cnt = 0 if v[i][j] else 1
    v[i][j] = 1
    while dq:
        ci, cj = dq.popleft()

        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and not arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + 1
                dq.append([ni, nj])
                cnt += 1
    
    return cnt, v

v = [[0] * N for _ in range(N)]

for ci, cj in start:
    cnt, v = bfs(ci-1, cj-1, v)
    answer += cnt

print(answer)

