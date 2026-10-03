# 격자: N x N
# 1 이상 N x N 이하의 수들이 한 번 씩만 등장

# 수의 이동
# M 번
# 1이 적힌 위치에서부터 N x N이 적힌 위치까지 순서대로
# 각 위치에서 8방향으로 인접한 칸들 중 가장 큰 수와 가운데 칸의 수를 교환


import sys

input = sys.stdin.readline


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def find_idx(value):
    for j in range(N):
        for k in range(N):
            if arr[j][k] == value:
                return j, k

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

for _ in range(M):
    for i in range(1, N * N+1):
        ci, cj  = find_idx(i)        
        max_val = [0, ci, cj]
        max_coord = []
        # 8 방향
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj):
                if arr[ni][nj] > max_val[0]:
                    max_val[0] = arr[ni][nj]
                    max_val[1], max_val[2] = ni, nj

        # 교환
        tmp = arr[ci][cj]
        arr[ci][cj] = arr[max_val[1]][max_val[2]]
        arr[max_val[1]][max_val[2]] = tmp

for row in arr:
    print(*row)
        # print('---------')