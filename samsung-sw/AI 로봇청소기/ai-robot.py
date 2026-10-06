# 격자: N x N
    # 좌상단: (1, 1)
    # 우하단: (N, N)

    # (1) 먼지가 있거나 / (2) 아무런 먼지가 없거나 / (3) 물건이 위치할 수 있다

    # 먼지가 있는 공간은 1에서 100사이의 먼지 양(p)를 가짐
    # 각 로봇 청소기는 초기 위치를 가지며, 해당 위치에는 먼지가 없음이 보장

# 테스트
    # [1] 청소기 이동
        # 각 청소기는 순서대로 이동거리가 가장 가까운 오염된 격자로 이동
        # 물건(-1)이 위치한 격자나 청소기(-2)가 있는 격자로 이동 불가
        # 이동 거리는 상하좌우로 인접한 격자를 한 칸씩 이동하여 도달하는데 필요한 최소 이동 횟수 (BFS)
        # 가장 가까운 격자가 여러개일 때, 행 번호 작은 -> 열 번호 작은
        
        # bfs 돌리고 [이동거리, i, j] return, sort 후 0번
    
    # [2] 청소
        # 바라보고 있는 방향 기준으로, 본인이 위치한 격자, 자신 왼쪽 오른쪽 귀쪽 격자를 청소할 수 있음
        # 청소할 수 있는 4가지 격자에서 청소할 수 있는 먼지량이 가장 큰 방향에서 청소 시작
        # 최대 청소량은 20
        # 합이 같은 방향이 여러개인 경우, 우,하,좌,상 순위
        # 청소는 청소기마다 순서대로 진행

    # [3] 먼지 축적
        # 먼지가 있는 모든 격자에 동시에 5씩 추가

    # [4] 먼지 확산
        # 깨끗한 격자에 주변 4방향 격자의 먼지량을 10으로 나눈 값만큼 먼지가 확산
        # 소수점 아래 버림
        # 모든 깨끗한 격자에 대해 동시에 확산 진행

    # [5] 출력
        # 전체 공간의 총 먼지량
        # 먼지가 있는 곳이 없으면 0을 출력후, 테스트 종료

    # L번 반복

import sys
from collections import deque

input = sys.stdin.readline


def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-------')


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


def bfs(i, j):
    # if arr[i][j] > 0:
    #     return i, j

    v = [[0] * N for _ in range(N)]
    v[i][j] = 1

    q = deque([[i, j]])

    lst = []
    #
    best = (N*N, i, j)
    # 
    while q:
        ci, cj = q.popleft()
        if arr[ci][cj] > 0:
            lst.append((v[ci][cj], ci, cj))

        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 물건(-1) 또는 청소기(-2)가 있는 격자로 이동 불가
            if in_range(ni, nj) and not v[ni][nj] and (arr[ni][nj] != -1 and d_arr[ni][nj] != -2):
                v[ni][nj] = v[ci][cj] + 1
                q.append([ni, nj])

                if arr[ni][nj] > 0:
                    candidate = (v[ni][nj], ni, nj)

                    if best is None or candidate < best:
                        best = candidate
    return lst
    # if best is None:
    #     return i, j   

    # _, i, j = best
    # return i, j


def move(devices):
    for idx, (id, i, j) in enumerate(devices):
        # 이동거리가 가장 가까운 오염된 격자로 이동
        # ei, ej = bfs(i, j)
        lst = bfs(i, j)
        
        if len(lst) > 0: # 먼지가 없는 공간에 고립된 청소기는 lst가 없을 수 있음
            # 가장 가까운 격자가 여러개일 때, 행 번호 작은 -> 열 번호 작은
            # lst.sort(key=lambda x: (x[0], x[1], x[2]))
            _, ei, ej = min(lst)
            
            d_arr[i][j] = 0
            d_arr[ei][ej] = -2
            devices[idx] = [id, ei, ej]


def clean(arr, devices):
    for idx, (id, i, j) in enumerate(devices):
        max_val = -1
        for dir in range(4):
            val = 0
            if dir == 0:  # 오른쪽 바라볼 때
                dis, djs = (0, -1, 1, 0), (0, 0, 0, 1)
                for di, dj in zip(dis, djs):
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        if arr[ni][nj] > 20:
                            val += 20
                        else:
                            val += arr[ni][nj]

            elif dir == 1:  # 아래 바라볼 때
                dis, djs = (0, 0, 1, 0), (0, -1, 0, 1)
                for di, dj in zip(dis, djs):
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        if arr[ni][nj] > 20:
                            val += 20
                        else:
                            val += arr[ni][nj]

            elif dir == 2:  # 왼쪽 바라볼 때
                dis, djs = (0, -1, 1, 0), (0, 0, 0, -1)
                for di, dj in zip(dis, djs):
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        if arr[ni][nj] > 20:
                            val += 20
                        else:
                            val += arr[ni][nj]

            elif dir == 3:  # 위 바라볼 때
                dis, djs = (0, 0, -1, 0), (0, 1, 0, -1)
                for di, dj in zip(dis, djs):
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        if arr[ni][nj] > 20:
                            val += 20
                        else:
                            val += arr[ni][nj]

            # val = 80 if val > 80 else val
            if max_val < val:
                max_val = val
                didj = [dis, djs]

        dis, djs = didj
        for di, dj in zip(dis, djs):
            ni, nj = i + di, j + dj
            if in_range(ni, nj) and arr[ni][nj] > 0:
                if arr[ni][nj] > 20:
                    arr[ni][nj] = arr[ni][nj] - 20
                else:
                    arr[ni][nj] = 0

    return arr

def spread(arr):
    n_arr = [x[:] for x in arr]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                val = 0
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ni, nj = i + di, j + dj
                    if in_range(ni, nj) and arr[ni][nj] > 0:
                        val += arr[ni][nj]
                n_arr[i][j] = val // 10

    return n_arr


N, K, L = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
device = [list(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(K)]

# 청소기 arr에 등록
d_arr = [x[:] for x in arr]
for i, j in device:
    d_arr[i][j] = -2

# device에 idx 등록
devices = []
for idx, (i, j) in enumerate(device):
    devices.append([idx + 1, i, j])

# 테스트 시작
# print_map(arr)
for l in range(L):
    # [1] 청소기 이동
    move(devices)
    # print_map(d_arr)

    # [2] 청소
    arr = clean(arr, devices)
    # print_map(arr)

    # [3] 먼지 축적: 먼지가 있는 모든 격자에 동시에 5씩 추가
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                arr[i][j] += 5
    # print_map(arr)

    # [4] 먼지 확산
        # 깨끗한 격자에 주변 4방향 격자의 먼지량을 10으로 나눈 값만큼 먼지가 확산
        # 소수점 아래 버림
        # 모든 깨끗한 격자에 대해 동시에 확산 진행
    n_arr = spread(arr)
    arr = n_arr
    # print_map(arr)

    # [5] 출력
        # 전체 공간의 총 먼지량
        # 먼지가 있는 곳이 없으면 0을 출력후, 테스트 종료
    total = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                total += arr[i][j]

    if total == 0:
        print(0)
        break

    else:
        print(total)