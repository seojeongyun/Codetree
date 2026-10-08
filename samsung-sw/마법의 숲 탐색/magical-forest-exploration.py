from collections import deque

# 격자(숲): R x C
    # 가장 위를 1행, 가장 아래를 R행
    # 격자의 동, 서, 남은 벽으로 막혀있음
    # 정령들은 북쪽에서 숲으로 들어옴

# 골렘
    # K명의 정령이 골렘을 타고 숲을 탐색
    # 골렘은 십자 모양 구조, 중앙칸을 포함해 5칸 차지
    # 중앙을 제외한 나머지 한 칸은 출구
    # 정령은 어떤 방향에서도 골렘에 탑승할 수 있지만, 내릴 땐 정해진 출구로만 내림
    # 초기 골렘의 출구는 di(0~3, 북동남서에 대응)의 방향에 위치

# 숲 탐색
    # i번째로 숲을 탐색하는 골렘은 숲의 북쪽 바깥에서 시작
    # 골렘의 중앙이 ci열이 되도록 하는 위치에서 내려오기 시작

    # [1] 남쪽으로 한 칸 이동
    # [2] 남쪽으로 한 칸 이동할 수 없으면 서쪽 방향으로 회전하면서 내려감
        # 그림에서 초록색 칸들이 비어있는 경우에만 회전하며 내려갈 수 있음
        # 출구가 반시계 방향으로 이동
    # [3] [1]과 [2]로 이동할 수 없으면 동쪽 방향으로 회전하면서 내려감
        # 그림에서 초록색 칸들이 비어있는 경우에만 회전하며 내려갈 수 있음
        # 출구가 시계 방향으로 이동
    # [4] 정령의 이동
        # 골렘이 이동할 수 있는 가장 남쪽에 위치해 더이상 이동할 수 없으면 정령은 골렘 내에서 상하좌우 인접 칸으로 이동
        # 현재 위치하고 있는 골렘의 출구가 다른 골렘과 인접하고 있으면, 해당 출구를 통해 다른 골렘으로 이동
        # 갈 수 있는 코든 칸 중 가장 남쪽의 칸으로 이동하고 이동을 종료
        # 이 때의 위치가 정령의 최종 위치

# 정령의 최종 위치의 행 번호의 합을 구해야함.
    # 골렘의 몸 일부가 숲을 벗어난 상태라면, 해당 골렘을 포함해 숲에 위치한 모든 골렘들은 숲을 빠져나간 뒤 다음 골렘부터 새롭게 숲을 탐색
    # 이 경우에는 정령이 도달하는 최종 위치를 답에 포함시키지 않음
    # 숲이 텅 비어도 행의 총합은 누적됨
# ------------------------------------------
def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:3}' for x in row))
    print('------------------------')
# ------------------------------------------
def in_range(i, j):
    return 0 <= i < R+3 and 0 <= j < C
# ------------------------------------------
def setup(arr, idx, si, sj, dir): # 골렘 초기 위치 그리기
    ci, cj = si, sj
    arr[ci][cj] = -(idx+1)
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        if in_range(ni, nj):
            arr[ni][nj] = -(idx + 1)

    ei, ej = ci + dis[dir], cj + djs[dir]
    arr[ei][ej] = (idx + 1)
    return arr
# ------------------------------------------
def move_south(arr, si, sj, dir):
    ci, cj = si, sj
    lst = []
    for di, dj in ((1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        lst.append([ni, nj])

    for i, j in lst:
        ni, nj = i + 1, j
        if not in_range(ni, nj):
            return False, arr, -1, -1
        elif arr[ni][nj] != 0:
            return False, arr, -2, -2

    # 골렘 좌표 갱신
    idx = -(arr[ci][cj]+1)
    golem[idx][0] += 1

    # 이전 위치 arr 0으로 초기화
    arr[ci][cj] = 0
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = ci + di, cj + dj
        if in_range(ni, nj):
            arr[ni][nj] = 0

    arr = setup(arr, idx, golem[idx][0], golem[idx][1], dir)
    return True, arr, golem[idx][0], golem[idx][1]
# ------------------------------------------
def move_left_rot(arr, si, sj, dir):
    lst = []
    for di, dj in ((-1, 0), (1, 0), (0, -1)):
        ni, nj = si + di, sj + dj
        lst.append([ni, nj])

    # 옆 체크
    for i, j in lst:
        ni, nj = i, j-1
        if not in_range(ni, nj) or arr[ni][nj] != 0:
            return False, arr

    # 아래 체크
    mi, mj = si+1, sj-1
    for di, dj in ((1, 0), (0, -1)):
        ni, nj = mi + di, mj + dj
        if not in_range(ni, nj) or arr[ni][nj] != 0:
            return False, arr

    # 여기까지 왔다면 비어있다는 의미
    # 골렘 좌표 및 dir 갱신
    idx = -(arr[si][sj]+1)
    golem[idx][0] += 1
    golem[idx][1] += -1
    golem[idx][2] = (dir-1+4)%4

    # 이전 위치 arr 0으로 초기화
    arr[si][sj] = 0
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = si + di, sj + dj
        if in_range(ni, nj):
            arr[ni][nj] = 0

    arr = setup(arr, idx, golem[idx][0], golem[idx][1], golem[idx][2])
    return True, arr

# ------------------------------------------
def move_right_rot(arr, si, sj, dir):
    lst = []
    for di, dj in ((-1, 0), (1, 0), (0, 1)):
        ni, nj = si + di, sj + dj
        lst.append([ni, nj])

    # 옆 체크
    for i, j in lst:
        ni, nj = i, j + 1
        if not in_range(ni, nj) or arr[ni][nj] != 0:
            return False, arr

    # 아래 체크
    mi, mj = si+1, sj+1
    for di, dj in ((1, 0), (0, 1)):
        ni, nj = mi + di, mj + dj
        if not in_range(ni, nj) or arr[ni][nj] != 0:
            return False, arr

    # 여기까지 왔다면 비어있다는 의미
    # 골렘 좌표 및 dir 갱신
    idx = -(arr[si][sj] + 1)
    golem[idx][0] += 1
    golem[idx][1] += 1
    golem[idx][2] = (dir + 1) % 4

    # 이전 위치 arr 0으로 초기화
    arr[si][sj] = 0
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        ni, nj = si + di, sj + dj
        if in_range(ni, nj):
            arr[ni][nj] = 0

    arr = setup(arr, idx, golem[idx][0], golem[idx][1], golem[idx][2])
    return True, arr
# ------------------------------------------
def move(moved_golem_lst):
    i, j, dir = moved_golem_lst
    #
    v = [[0] * C for _ in range(R + 3)]
    v[i][j] = 1
    #
    q = deque([[i, j]])
    #
    max_i = -1
    #
    while q:
        ci, cj = q.popleft()
        #
        if max_i < ci:
            max_i = ci
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            # if in_range(ni, nj) and not v[ni][nj] and (arr[ni][nj] == -arr[ci][cj] or (arr[ci][cj] > 0 and arr[ni][nj] > 0) or arr[ci][cj] == arr[ni][nj]) and arr[ni][nj] != 0:
            if in_range(ni, nj) and not v[ni][nj] and (arr[ni][nj] == -arr[ci][cj] or arr[ci][cj] > 0 or arr[ci][cj] == arr[ni][nj]) and arr[ni][nj] != 0:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1

    return max_i-2
# ------------------------------------------
# ------------------------------------------
R, C, K = map(int, input().split())
g_lst = [list(map(int, input().split())) for _ in range(K)]
golem = []
for j, dir in g_lst:
    golem.append([1, j-1, dir])

answer = 0

arr = [[0] * C for _ in range(R+3)]
dis, djs = (-1, 0, 1, 0), (0, 1, 0, -1)
# ------------------------------------------
for idx, (si, sj, dir) in enumerate(golem):
    clear = False
    arr = setup(arr, idx, si, sj, dir)

    # [1] 골렘의 이동: 남쪽
    while True:
        # 남쪽으로 한 칸 이동 가능한지 확인
        move_success, arr, si, sj = move_south(arr, si, sj, dir)
        if (si, sj) == (-1, -1): # 바닥에 닿았으면 break
            break

        elif (si, sj) == (-2, -2):
        # [2] 골렘의 이동: 서쪽방향으로 회전하면서 내려갈 수 있는지 확인
            while True:
                left_rot_success, arr = move_left_rot(arr, golem[idx][0], golem[idx][1], golem[idx][2])
                if left_rot_success:
                    while True:
                        move_success, arr, si, sj = move_south(arr, golem[idx][0], golem[idx][1], golem[idx][2])
                        if not move_success:
                            break
                if not left_rot_success:
                    break

            # [3] 골렘의 이동: 동쪽 방향으로 회전하면서 내려갈 수 있는지 확인
            while True:
                right_rot_success, arr = move_right_rot(arr, golem[idx][0], golem[idx][1], golem[idx][2])
                if right_rot_success:
                    while True:
                        move_success, arr, si, sj = move_south(arr, golem[idx][0], golem[idx][1], golem[idx][2])
                        if not move_success:
                            break
                if not right_rot_success:
                    break

            break

    # print_map(arr)

    # 숲 clear 조건 체크
    for i in range(3):
        if sum(arr[i][:]) != 0:
            clear = True
            arr = [[0] * C for _ in range(R + 3)]

    # [4] 정령의 이동:
    if clear: continue
    answer += move(golem[idx])
    # print(answer)
    # None

print(answer)
    # print(golem[idx])