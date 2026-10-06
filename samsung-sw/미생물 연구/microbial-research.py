# 격자: N x N

# 실험
    # Q번 진행

    # [1] 미생물 투입
        # 좌하단 좌표: (r1, c1), 우상단 좌표: (r2, c2)인 직사각형 영역에 미생물 투입
        # 영역 내 다른 미생물이 존재하면 덮어쓰기
        # 기존 무리가 새로 투입된 무리에 의해 두 그룹으로 나누어지면, 기존 무리는 사라짐

    # [2] 배양 용기 이동
        # 기존 배양 용기에 있는 모든 미생물을 이동
        # 우선 순위
            # 차지한 영역이 가장 넓은 -> 먼저 투입된
        # 기존 용기에서의 형태를 유지
            # x 작은 -> y 작은
        # 어떤 곳에도 둘 수 없는 미생물은 사라짐

    # [3] 실험 결과 기록
        # 인접한 무리: 미생물 무리 중 상하좌우로 닿은 면이 있는 무리
        # 모든 인접한 무리 쌍을 확인
            # A와 B가 맞닿은 면이 둘 이상이더라도 한 번만 체크
        # A와 B가 인접한 무리라면, 미생물 A의 영역 넓이 * 미생물 B의 영역 넓이 만큼이 성과
        # 확인한 모든 쌍의 성과를 더한 값이 실험의 결과

import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline

def print_arr(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('----------')
# ----------------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N
# ----------------------------------------
def check(arr, v, i, j, c_num):
    coords = [[i, j]]
    #
    v[i][j] = 1
    area = 1
    #
    q = deque([[i, j]])
    adjacent = set()

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0),(1, 0),(0, 1),(0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] == c_num:
                v[ni][nj] = 1
                q.append([ni, nj])
                area += 1
                coords.append([ni, nj])
            if in_range(ni, nj) and arr[ni][nj] != 0 and arr[ni][nj] != c_num:
                adjacent.add((c_num, arr[ni][nj]))

    return area, v, coords, adjacent
# ----------------------------------------
def move(k):
    # offset
    valid = True
    for offset_x in range(N - 1, -N, -1):
        for offset_y in range(N - 1, -N, -1):
            lst = []
            for ci, cj in unit_dict[k][0]:
                ni, nj = ci - offset_y, cj - offset_x
                if in_range(ni, nj) and new_arr[ni][nj] == 0:
                    lst.append([ni, nj])
            if len(lst) == unit_dict[k][1]:
                unit_dict[k][0] = lst
                return lst

    return []
# ----------------------------------------

# ----------------------------------------

N, Q = map(int, input().strip().split())
units = [list(map(int, input().strip().split())) for _ in range(Q)]
arr = [[0] * N for _ in range(N)]

answer = []
# arr랑 lst로 각각 관리. arr은 bfs를 위해, lst는 여러 상태를 위해.

unit_dict = {} # 좌표, area, valid

# Q번 실험 진행
for idx, (c1, r1, c2, r2) in enumerate(units):
    v = [[0] * N for _ in range(N)]
    #
    # [1] 미생물 투입
    for i in range(r1, r2):
        for j in range(c1, c2):
            arr[i][j] = idx + 1

    # print_arr(arr)

    # 격자내 존재하는 미생물 Id 획득
    sset = set()
    for i in range(N):
        for j in range(N):
            if arr[i][j] and arr[i][j] not in sset:
                sset.add(arr[i][j])

    # 완전히 덮어씌워진 미생물이 있는지 검사
    for k in (set(unit_dict.keys()) - sset):
        unit_dict[k] =unit_dict[key] = [[-1, -1], 0, 0]

    # 격자 내 존재하는 미생물이 두 그룹으로 나뉘었는지 확인
    for key in sset:
        #
        num_cluster = 0
        for i in range(N):
            for j in range(N):
                if not v[i][j] and arr[i][j] == key:
                    num_cluster += 1
                    area, v, coords, _ = check(arr, v, i, j, key)
        if num_cluster > 1:
            # 어차피 배양용기 옮길 거라서 굳이 현재 arr에서 0 처리 안해줘도 될듯
            unit_dict[key] = [[-1, -1], 0, 0]
        else:
            unit_dict[key] = [coords, area, 1]

    #
    # [2] 배양 용기 이동
    new_arr = [[0] * N for _ in range(N)]
    sorted_keys = sorted(unit_dict.keys(), key=lambda x: (-unit_dict[x][1], x))  # 영역 -> 투입 순서 소팅

    for k in sorted_keys:
        if unit_dict[k][0] == [-1, -1]: continue
        lst = move(k)

        if lst == []: # 어디에도 둘 수 없는 경우
            unit_dict[k] = [[-1, -1], 0, 0]
        else:
            for i, j in unit_dict[k][0]:
                new_arr[i][j] = k
            #
            unit_dict[k][0] = lst
    # print_arr(new_arr)
    arr = new_arr

    # [3] 실험 결과 기록
    # 인접한 무리 찾아 인덱스 리턴하기
    adjacent_v = [[0] * N for _ in range(N)]
    adjacent_lst = []
    for k in unit_dict.keys():
        if unit_dict[k][0] == [-1, -1]: continue
        for i in range(N):
            for j in range(N):
                if not adjacent_v[i][j] and arr[i][j] == k:
                    _, adjacent_v, _, adjacent = check(arr, adjacent_v, i, j, k)
                    adjacent_lst.append(adjacent)

    if len(adjacent_lst) == 0:
        print(0)

    else:
        # adjacent_lst 중복 제거
        adj_lst = []
        for adjacent in adjacent_lst:
            for adj in adjacent:
                a = sorted(list(adj))
                if a not in adj_lst:
                    adj_lst.append(a)

        sum = 0
        for v1, v2 in adj_lst:
            sum = sum + (unit_dict[v1][1] * unit_dict[v2][1])
        print(sum)
    # [3] 실험 결과 기록
        # 인접한 무리: 미생물 무리 중 상하좌우로 닿은 면이 있는 무리
        # 모든 인접한 무리 쌍을 확인
            # A와 B가 맞닿은 면이 둘 이상이더라도 한 번만 체크
        # A와 B가 인접한 무리라면, 미생물 A의 영역 넓이 * 미생물 B의 영역 넓이 만큼이 성과
        # 확인한 모든 쌍의 성과를 더한 값이 실험의 결과