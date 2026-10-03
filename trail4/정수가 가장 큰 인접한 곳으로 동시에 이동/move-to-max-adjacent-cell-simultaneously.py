# 격자: N x N

# 구슬의 이동
    # M개의 구슬이 서로 다른 위치에서 시작
    # 1초에 한 번 씩 상하좌우 중 가장 큰 값이 적힌 곳으로 동시에 이동

# 구슬의 충돌
    # 이동 후 2개 이상의 구슬 위치가 동일하면 해당 위치에 있는 구슬은 모두 사라짐

# T초 후 남아있는 구슬의 수를 출력

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def moves(pos):
    moved_pos = []
    for r, c in pos:
        ci, cj = r-1, c-1
        mi, mj = ci, cj
        max_val = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj):
                if max_val < arr[ni][nj]:
                    max_val = arr[ni][nj]
                    mi, mj = ni, nj
        
        moved_arr[mi][mj] += 1
    return moved_pos

def is_crashed():
    lst = []
    for i in range(N):
        for j in range(N):
            if moved_arr[i][j] == 1:
                lst.append([i+1, j+1])

    return lst

# 입력
N, M, T = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
pos = [list(map(int, input().strip().split())) for _ in range(M)]

# T초
for _ in range(T):
    moved_arr = [[0] * N for _ in range(N)]

    # 구슬의 이동
    if len(pos) > 0:
        pos = moves(pos)

    # 충돌 여부 확인
    pos = is_crashed()


print(len(pos))
