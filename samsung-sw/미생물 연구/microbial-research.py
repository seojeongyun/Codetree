# 격자: N x N
# 실험
    # Q번 진행
        # [1] 미생물 투입
            # 좌상단 좌표가 (r1, c1)이고 우하단 좌표가 (r2, c2)인 직사각형 영역에 한 무리의 미생물 투입
            # 영역 내에 다른 미생물이 존재한다면 덮어쓰기
                # 덮어씌워지면서 기존 미생물이 두 무리로 나뉘어지면 배양 용기에서 아예 사라짐

        # [2] 배양 용기 이동
            # 새로운 배양 용기로 이동(기존 용기와 크기 동일)
                # 기존 배양 용기에 미생물이 한 마리도 남지 않을 때 까지 반복
            # 미생물 이동 우선 순위:
                # 기존 용기에 있는 무리 중 영역이 가장 넓은 무리
                # 투입 순서
            # 이동시 기존 용기에서의 형태를 유지해야하며, 범위 내에 있어야하고, 다른 미생물의 영역과 겹치지 않아야 함
                # 이 조건을 만족하면서 최대한 x좌표가 작은 위치로 옮겨야하며, 그런 위치가 둘 이상인 경우 최대한 y좌표가 작은 위치로 오도록 옮김
                # 어떤 곳에도 둘 수 없는 미생물 무리가 있는 경우 새 용기에 옮겨지지 않고 사라짐

        # [3] 실험 결과 기록
            # 미생물 무리 중 상하좌우로 맞닿은 면이 있는 무리끼리는 '인접한 무리'라고 표현
            # 인접한 무리 쌍을 확인. 두 무리 A와 B가 맞닿은 면이 둘 이상이더라도 (A,B) 쌍은 한 번만 확인
            # 두 무리가 A, B라면 (A의 넓이) * (B의 넓이) 만큼의 성과를 얻음
            # 확인한 모든 쌍의 성과를 더한 값이 실험의 결과.

# 실험의 결과를 출력하는 프로그램 작성

import sys
from collections import deque

input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:3}' for x in row))

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def bfs(arr, v, i, j, c_num):
    dq = deque([(i, j)])
    area = 1
    #
    while dq:
        ci, cj = dq.popleft()
        #
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di , cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] == c_num:
                v[ni][nj] = c_num
                dq.append((ni, nj))
                area += 1

    return v, area

def is_devide(arr, creatures_lst):
    v = [[0] * N for _ in range(N)]
    #
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j]:
                v[i][j] = arr[i][j]
                v, area = bfs(arr, v, i, j, arr[i][j])
                for idx, (c_num, _, _, _) in enumerate(creatures_lst):
                    if c_num == arr[i][j]:
                        creatures_lst[idx][1] += 1
                        creatures_lst[idx][2] = area

    return creatures_lst


def put_creatures(arr, creatures_lst, creature, exp_idx):
    removed_creature = []

    # 미생물 투입 및 덮어쓰기
    c1, r1, c2, r2 = creature
    # c_num, cluster_num, area, coords
    creatures_lst.append([exp_idx+1, 0, 0, []])
    # 미생물 투입 및 덮어쓰기
    for r in range(r1, r2):
        for c in range(c1, c2):
            if arr[r][c] != 0:
                for idx, (c_num, _, _, _) in enumerate(creatures_lst):
                    if c_num == arr[r][c]:
                        creatures_lst[idx][-1].remove([r,c])
                        if len(creatures_lst[idx][-1]) == 0:
                            creatures_lst.pop(idx)
            arr[r][c] = (exp_idx + 1)
            creatures_lst[-1][-1].append([r,c])

    # 기존 미생물이 두 개의 그룹으로 나뉘었는지 여부 확인
    creatures_lst = is_devide(arr, creatures_lst)
    for idx, (c_num, _, _, _) in enumerate(creatures_lst):
        # 두 그룹 이상이면 해당 위치 값 0으로 초기화
        if creatures_lst[idx][1] > 1:
            removed_creature.append(idx)
            for i in range(N):
                for j in range(N):
                    if arr[i][j] == c_num:
                        arr[i][j] = 0

    # 딕셔너리 idx 0 값 초기화: 초기화 안하면 미생물 투입될 때 마다 값 누적되어 cluster 개수 파악 안됨
    for i in range(len(creatures_lst)):
        creatures_lst[i][1] = 0

    for idx in sorted(removed_creature, reverse=True):
        creatures_lst.pop(idx)

    return arr, creatures_lst

def move_arr(new_arr, lst):
    # 기존 용기에서의 형태 유지, 범위 내, 다른 미생물 영역과 겹치지 않게.
    # x좌표가 가장 작은 위치로 옮김, 그런 위치가 둘 이상이면 y좌표가 작은 위치로 옮김
    # 어느곳으로도 옮길 수 없으면 사라짐
    c_num, _, _, coords = lst

    # 제일 왼쪽에 있는 좌표가 occupied_max_x+1로 올 수 있게
    coords.sort(key=lambda x: (x[1], x[0]))
    min_x, min_y = coords[0]
    #
    # 완전 탐색
    for x in range(N-1, -N, -1):
        x_offset = min_x - x
        for y in range(N-1, -N, -1):
            new_coords = []
            y_offset = min_y - y
            for i, j in coords:
                ni = i - y
                nj = j - x
                if not in_range(ni, nj) or new_arr[ni][nj] != 0:
                    break
                new_coords.append([ni, nj])
            else:
                for i, j in new_coords:
                    new_arr[i][j] = c_num
                return new_arr, new_coords, False

    # 여기까지 왔다면 버려야 하는 미생물인 것
    return new_arr, _, True

def cluster_bfs(arr, cluster_v, i, j, c_num):
    dq2 = deque([(i, j)])
    adjacent_cluster_lst = []
    while dq2:
        ci, cj = dq2.popleft()
        #
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not cluster_v[ni][nj] and arr[ni][nj] == c_num:
                cluster_v[ni][nj] = c_num
                dq2.append([ni, nj])

            if in_range(ni, nj) and not cluster_v[ni][nj]:
                if arr[ni][nj] != c_num and arr[ni][nj] != 0:
                    if [c_num, arr[ni][nj]] not in adjacent_cluster_lst:
                        adjacent_cluster_lst.append([c_num, arr[ni][nj]])

    return adjacent_cluster_lst

def get_adjacent_cluster(arr):
    cluster_v = [[0] * N for _ in range(N)]
    lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] and not cluster_v[i][j]:
                cluster_v[i][j] = arr[i][j]
                adjacent_cluster_lst = cluster_bfs(arr, cluster_v, i, j, arr[i][j])
                if len(adjacent_cluster_lst) != 0:
                    lst.append(adjacent_cluster_lst)

    return lst

# 입력
N, Q = map(int, input().strip().split())
creatures = [list(map(int, input().strip().split())) for _ in range(Q)]

# Q번 실험 진행
arr = [[0] * N for _ in range(N)]
creatures_lst = []
#
for exp_idx in range(Q):
    # [1] 미생물 투입
    creatures_lst.sort(key=lambda x: x[0])
    arr, creatures_lst = put_creatures(arr, creatures_lst, creatures[exp_idx], exp_idx)

    # [2] 배양 용기 이동
    new_arr = [[0] * N for _ in range(N)]

    creatures_lst.sort(key=lambda x: (-x[2], x[0]))
    new_creatures_lst = []
    offset = 0
    for i, lst in enumerate(creatures_lst):
        new_arr, new_coords, is_removed = move_arr(new_arr, lst)
        if is_removed:
            pass
        else:
            new_creatures_lst.append(creatures_lst[i])
            new_creatures_lst[-1][-1] = new_coords

    # 새 배양 용기 상태 arr에 복사: 다음 미생물 넣을 때 이거 써야함
    arr = [row[:] for row in new_arr]
    creatures_lst = new_creatures_lst[:]
    # print_map(arr)

    # [3] 실험 결과 기록
    # 인접한 무리 구하기
    adj_lst = get_adjacent_cluster(arr)
    # print(adj_lst)

    # 성과 구하기
    score = 0
    for adj_cluster_from_a_creature_lst in adj_lst:
        for adj_cluster_lst in adj_cluster_from_a_creature_lst:
            score_ = 1
            for c_num_ in adj_cluster_lst:
                for idx, (c_num, _, area, _) in enumerate(creatures_lst):
                    if c_num == c_num_:
                        score_ *= creatures_lst[idx][2]
            score += score_
    print(score)
