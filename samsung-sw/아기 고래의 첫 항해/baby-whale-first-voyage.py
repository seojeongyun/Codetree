from collections import deque


# 격자 : N x N
# 헤엄칠 수 있는 바다 (0) / 지나갈 수 없는 암초 (1)

# 아기고래
# 초기 위치 (r, c)
# 초기 방향 d
# 1,2,3,4 - 상,하,좌,우

# 탐험
# [1] 인접 탐험
# 현재 위치에서 상하좌우로 인접한 칸 중 아직 방문하지 않은 바다칸을 방문
# 우선순위
# 현재 바라보는 방향으로 직진
# 좌회전 후 직진
# 우회전 후 직진
# 180도 회전 후 직진
# 이동하면 바라보는 방향은 이동한 방향으로 갱신
# 인접한 칸에 방문 가능한 바다가 없을 때 까지 반복

# [2] 가장 가까운 바다로 이동
# 인접한 칸에 방문 가능한 바다가 없다면, 아직 방문하지 않은 칸 중 현재 위치에서 가장 가까운 바다로 이동
# 가장 가까운 -> 거리는 상하좌우로 인접한 칸을 한 칸 씩 이동하며 도달하는데 필요한 최소 이동 횟수
# 가장 가까운 칸이 여러개면, 행 작은 -> 열 작은
# 선택한 칸 까지 최단 거리로 이동
# 매 이동마다 선택한 칸까지의 거리가 1 줄어드는 인접한 칸 중 하나로 이ㅗㅇ
# 여러개면 좌하우상 순서
# 도착 후 바라보는 방향은 마지막 이동 방향

# 헤엄칠 수 있는 모든 바다를 방문할 때 까지 위 과정 반복
# 방문하는 바다 칸의 위치를 순서대로 출력

# ------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


# ------------------------------
def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-----------------')


# ------------------------------
def is_end(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                return False

    return True


# ------------------------------
def first_move(i, j, dr):
    ci, cj = i, j
    #
    arr[ci][cj] = -1
    #
    while True:
        ni, nj = ci + dis[dr], cj + djs[dr]
        while in_range(ni, nj) and arr[ni][nj] == 0:
            arr[ni][nj] = -1
            answer.append([ni + 1, nj + 1])
            ci, cj = ni, nj
            ni, nj = ci + dis[dr], cj + djs[dr]
            if not in_range(ni, nj): break
        ci, cj = ni - dis[dr], nj - djs[dr]

        # 방향 바꾸기: 좌회전 후 직진 -> 우회전 후 직진 -> 180도 회전 후 직진
        for n_dr in ((dr - 1 + 4) % 4, (dr + 1) % 4, (dr + 2) % 4):
            wi, wj = ci + dis[n_dr], cj + djs[n_dr]
            if in_range(wi, wj) and not arr[wi][wj]:
                dr = n_dr
                break

        else:
            break

    return ci, cj


# ------------------------------
def bfs_get_closest(i, j):
    q = deque([[i, j]])
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1
    lst = []

    while q:
        ci, cj = q.popleft()
        #
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] != 1:
                v[ni][nj] = v[ci][cj] + 1
                q.append([ni, nj])
                if arr[ni][nj] == 0:
                    lst.append([v[ni][nj] - 1, ni, nj])
    return lst


# ------------------------------
def bfs_get_route(i, j, ti, tj):
    q = deque([[i, j]])
    v = [[0] * N for _ in range(N)]
    v[i][j] = (i, j)
    route = [[ti, tj]]
    while q:
        ci, cj = q.popleft()
        #
        if (ci, cj) == (ti, tj):
            ci, cj = v[ci][cj]
            while (ci, cj) != (i, j):
                route.append([ci, cj])
                ci, cj = v[ci][cj]
            return route[::-1]

        for di, dj in ((0, -1), (1, 0), (0, 1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] != 1:
                v[ni][nj] = (ci, cj)
                q.append([ni, nj])

    return -1


# ------------------------------
def second_move(i, j, dr):
    dir = dr
    lst = bfs_get_closest(i, j)
    dist, ti, tj = min(lst)
    answer.append([ti + 1, tj + 1])

    # i,j -> ti, tj로 이동경로 획득
    route = bfs_get_route(i, j, ti, tj)
    if route == -1:
        print('route == -1')
    else:  # 방향 결정
        for n_ti, n_tj in route:
            for dr, di, dj in ((3, -1, 0), (1, 1, 0), (0, 0, 1), (2, 0, -1)):
                ni, nj = i + di, j + dj
                if in_range(ni, nj):
                    if (n_ti, n_tj) == (ni, nj):
                        arr[ni][nj] = -1
                        i, j = ni, nj
                        dir = dr
                        break
        return ti, tj, dir


# ------------------------------
# ------------------------------
# ------------------------------
# ------------------------------
N, i, j, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = []
#
ci, cj = i - 1, j - 1
answer.append([i, j])
#
# dis, djs: 1,2,3,4 - 상,하,좌,우
dis, djs = (0, 1, 0, -1), (1, 0, -1, 0)
dir_dict = {
    1: 3,
    2: 1,
    3: 2,
    4: 0
}
dir_num = dir_dict[d]
# 항해 시작
while True:
    # [1] 인접 탐험
    ci, cj = first_move(ci, cj, dir_num)
    # print_map(arr)

    # 종료 조건: 헤엄칠 수 있는 곳이 없다.
    if is_end(arr):
        break

    # [2] 가까운 바다로 이동
    ci, cj, dir_num = second_move(ci, cj, dir_num)

for i, j in answer:
    print(i, j)