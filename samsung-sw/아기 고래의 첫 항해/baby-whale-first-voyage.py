# 격자 : N x N
    # 헤엄칠 수 있는 바다: 0
    # 암초: 1

# 헤엄
    # 아기 고래 초기 위치: r, c
    # 처음 바라보는 방향은 d
        # 1: 상 / 2: 하 / 3: 좌 / 4: 우

# 탐험
    # 1. 인접 탐험
        # 상하좌우 인접한 칸 중 방문하지 않은 칸에 우선순위대로 한 칸 이동
            # 우선 순위
                # 현재 바라보는 방향으로 직진
                # 좌회전 후 직진 dir_num = (dir_num - 1 + 4) % 4
                # 우회전 후 직진 dir_num = (dir_num + 1) % 4
                # 180도 회전 후 직진 dir_num = (dir_num + 2) % 4
        # 이동 후, 바라보는 방향은 이동한 방향으로 갱신
        
        # 인접한 칸에 방문 가능한 바다가 없을 때 까지 반복

    # 2. 가장 가까운 바다로 이동
        # 아직 방문하지 않는 바다 칸 중 현재 위치에서 가장 가까운 칸으로 이동
            # 거리는 상하좌우로 인접한 칸을 한 칸 씩 이동하여 도달하는 데 필요한 최소 이동 횟수 (맨해튼 거리?)
                # 암초는 지나갈 수 없고, 이미 방문한 바다는 지나갈 수 있음
            # 가장 가까운 칸이 여러개면, 행 번호 작고 -> 열 번호가 작은 순으로 선택
            # 선택한 칸까지 최단 거리로 이동
                # 매 이동마다 선택한 칸까지의 거리가 1 줄어드는 인접한 칸 중 하나로 이동
                    # 그러한 칸이 여러개라면 좌, 하, 우, 상 순서로 선택
            # 도착 후 바라보는 방향은 마지막 이동 방향으로 갱신

# 위 과정을 반복하며 헤엄칠 수 있는 모든 바다를 방문하면 종료
# 방문하는 바다 칸의 위치를 방문 순서대로 출력, 시작 위치도 출력에 포함

import sys
from collections import deque

input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-----------')


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


def is_done(arr):
    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                return False

    return True


def get_manhattan(pos1, pos2):
    pos1_i, pos1_j = pos1
    pos2_i, pos2_j = pos2

    return abs(pos1_i - pos2_i) + abs(pos1_j - pos2_j)


def get_dist(start, end):
    i,j = start
    ei, ej = end
    
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    
    q = deque([start])
    
    while q:
        ci, cj = q.popleft()
        # 종료 조건
        if (ci, cj) == (ei, ej):
            return visited[ci][cj] - 1
        
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not arr[ni][nj] and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1
            

def get_closest(i, j):
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    q = deque([[i, j]])
    lst = []
    
    while q:
        ci, cj = q.popleft()
        # 종료 조건
        if not v[ci][cj]:
            lst.append([visited[ci][cj], ci, cj])

        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not arr[ni][nj] and not visited[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1

    return lst

# 입력
N, r, c, d = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = [[r, c]]

# di, dj # 1: 상 / 2: 하 / 3: 좌 / 4: 우
dis, djs = (0, 1, 0, -1), (1, 0, -1, 0)
dir_dict = {
    1: 3,
    2: 1,
    3: 2,
    4: 0
}
dir_num = dir_dict[d]

#
ci, cj = r - 1, c - 1
v = [x[:] for x in arr]
v[ci][cj] = 1

while True:
# for _ in range(5):
    # 인접 탐험: 인접한 칸에 방문 가능한 바다가 없을 때 까지 반복
    while True:
        valid = False

        # 종료 조건
        for try_num in range(4):
            if try_num == 0:
                dir_num_ = dir_num

            elif try_num == 1:  # 좌회전 후 직진
                dir_num_ = (dir_num - 1 + 4) % 4

            elif try_num == 2:  # 우회전 후 직진
                dir_num_ = (dir_num + 1) % 4

            elif try_num == 3:  # 180도 회전 후 직진
                dir_num_ = (dir_num + 2) % 4

            ni, nj = ci + dis[dir_num_], cj + djs[dir_num_]
            if in_range(ni, nj) and not v[ni][nj] and not arr[ni][nj]:
                v[ni][nj] = v[ci][cj] + 1
                answer.append([ni+1, nj+1])
                ci, cj = ni, nj
                valid = True
                dir_num = dir_num_
                break

        if not valid:
            break

        # print_map(v)

    # 종료 조건
    if is_done(v):
        break

    # 가장 가까운 바다로 이동
    # 아직 방문하지 않은 가장 가까운 칸 찾기 (행 번호 작고 -> 열 번호 작은), 기준은 맨해튼 거리 X. 암초 고려해야함 ******************************    
    lst = get_closest(ci, cj)
    lst.sort(key=lambda x: (x[0], x[1], x[2]))
    _, ei, ej = lst[0]
                    
    # print(ci, cj, ei, ej)
    # 인접 칸으로 이동: 암초는 지나갈 수 없고, 이미 방문한 바다는 지나갈 수 있음
    # 선택한 칸 까지의 거리가 1 줄어드는 인접한 칸 중 하나로 이동
    # 우선순위: 좌, 하, 우, 상
    moving = True
    while moving:
        for dir_num, di, dj in ((2, 0, -1), (1, 1, 0), (0, 0, 1), (3, -1, 0)):
            ni, nj = ci + di, cj + dj
            # 종료 조건
            if (ni, nj) == (ei, ej):
                moving = False
                break

            if in_range(ni, nj) and not arr[ni][nj] and (get_dist((ei, ej), (ci, cj)) - get_dist((ei, ej), (ni, nj)) == 1):
                ci, cj = ni, nj
                break

    v[ei][ej] = v[ci][cj] + 1
    # print_map(v)
    ci, cj = ei, ej
    answer.append([ci+1, cj+1])

for row in answer:
    print(*row)