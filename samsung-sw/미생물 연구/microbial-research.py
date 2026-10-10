from collections import deque


# 격자: N x N
# 좌하단 (0, 0), 우상단(N, N) -> 좌상단 우하단으로 치환

# 실험 (Q회)
# [1] 미생물 투입
# 좌상단(r1, c1), 우하단(r2,c2)인 영역에 미생물 투입
# 기존에 미생물 존재할 시 덮어쓰기 -> 기존 미생물이 두 그룹으로 나뉘면 기존 무리 사라짐

# [2] 배양 용기 이동
# 기존 배양 용기에 있는 무리 중 차지한 영역이 가장 넓음 무리
# 둘 이상이라면 먼저 투입된 미생물
# 기존 용기에서의 형태를 유지해야하며, x 작은 -> y 작은
# 어디에도 둘 수 없는 경우 사라짐

# [3] 실험 결과 기록
# 인접한 무리 A, B에 대해 A영역 넓이 * B영역 넓이가 성과
# 모든 인접한 무리 쌍에 대한 성과를 기록

# 매 실험마다의 실험 결과 출력

# -----------------------------
def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-------------------')


# -----------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


# -----------------------------
def bfs(v, i, j):
    q = deque([[i, j]])
    v[i][j] = 1
    area = 1
    while q:
        ci, cj = q.popleft()
        #
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] == arr[i][j]:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
                area += 1

    return area


# -----------------------------
def find_adjacent(arr, v, i, j):
    q = deque([[i, j]])
    v[i][j] = 1
    adj_set = set()
    while q:
        ci, cj = q.popleft()
        #
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] == arr[i][j]:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
            if in_range(ni, nj) and not v[ni][nj] and (arr[ni][nj] != arr[i][j] and arr[ni][nj] != 0):
                if (arr[i][j], arr[ni][nj]) not in adj_set and (arr[ni][nj], arr[i][j]) not in adj_set:
                    adj_set.add((arr[i][j], arr[ni][nj]))

    return adj_set


# -----------------------------

N, Q = map(int, input().split())
answer = []
units = []  # [투입 순서, 넓이, [좌표들]]
arr = [[0] * N for _ in range(N)]
# 실험 시작
for time in range(1, Q + 1):
    unit = [time, 0]
    #
    c1, r1, c2, r2 = map(int, input().split())
    v = [[0] * N for _ in range(N)]

    # 배양 용기에 담기
    coords = []
    removed_coords = []
    for i in range(r1, r2):
        for j in range(c1, c2):
            if arr[i][j] != 0:
                removed_coords.append([arr[i][j], i, j])
            arr[i][j] = time
            coords.append([i, j])
    unit.append(coords)
    units.append(unit)

    if len(removed_coords):
        for idx in range(len(units)-1 ,-1, -1):
            time, area, coords = units[idx]
            for t, i, j in removed_coords:
                if time == t:
                    if len(units[idx][-1]) > 1:
                        units[idx][-1].remove([i, j])
                    else:
                        units.pop(idx)

    # 기존 유닛이 두 그룹으로 나뉘었는지 확인
    sset = set()
    removed = set()
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j] > 0:
                if arr[i][j] in sset:
                    removed.add(arr[i][j])

                else:
                    sset.add(arr[i][j])
                    area = bfs(v, i, j)
                    for idx, (time, _, _) in enumerate(units):
                        if time == arr[i][j]:
                            units[idx][1] = area
                            break

    for num in removed:
        for idx in range(len(units) - 1, -1, -1):
            time, area, coords = units[idx]
            if time == num:
                for i, j in coords:
                    arr[i][j] = 0
                units.pop(idx)
                break

    # [2] 배양 용기 이동
    # 모든 좌표를 0에 대한 상대좌표로 변경
    for idx, (time, area, coords) in enumerate(units):
        mi, mj = min(coords)
        lst = []
        for i, j in coords:
            lst.append([i - mi, j - mj])
        units[idx][-1] = lst

    # x 작은 -> y 작은
    # 어디에도 둘 수 없는 경우 사라짐
    moved = set()
    new_arr = [[0] * N for _ in range(N)]
    units.sort(key=lambda x: (-x[1], x[0]))
    for idx, (time, area, coords) in enumerate(units):
        next = False
        coords_lst = []
        for j in range(N):
            for i in range(N):
                for ui, uj in coords:
                    ni, nj = ui + i, uj + j
                    if in_range(ni, nj) and not new_arr[ni][nj]:
                        coords_lst.append([ni, nj])
                    else:
                        coords_lst = []
                        break
                else:
                    moved.add(idx)
                    units[idx][2] = coords_lst
                    for ui, uj in coords_lst:
                        new_arr[ui][uj] = units[idx][0]
                    next = True
                    break
            if next:
                break

    for idx in range(len(units) - 1, -1, -1):
        if idx not in moved:
            units.pop(idx)

    # [3] 실험 결과 기록
    adj_lst = []
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j] and new_arr[i][j] > 0:
                adj_set = find_adjacent(new_arr, v, i, j)
                if len(adj_set) > 0 :
                    adj_lst.append(adj_set)

    score = 0
    for adj in adj_lst:
        for t1, t2 in adj:
            adj_score = 1
            for idx, (time, area, coords) in enumerate(units):
                if time == t1 or time == t2:
                    adj_score *= area
            score += adj_score

    arr = new_arr
    print(score)

    # 인접한 무리 A, B에 대해 A영역 넓이 * B영역 넓이가 성과
    # 모든 인접한 무리 쌍에 대한 성과를 기록

