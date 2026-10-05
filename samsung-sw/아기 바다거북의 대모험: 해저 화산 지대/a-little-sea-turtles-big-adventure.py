# 격자 : N x N
    # 안식처 위치 : N-1, N-1

# 시뮬레이션
    # 최대 100턴 진행

    # 1단계: 바다 거북 이동
        # ID가 작은 순서대로 한 마리씩 이동
        # 자신의 차례에 현재 바다 상태를 기준으로 안식처까지의 최단 경로 탐색
            # 장애물: 산호초(1), 다른 살아있는 바다거북(-1), 화석(-2)
            # 규칙: 최단 경로가 존재하면 해당 경로의 첫 번째 칸으로 한 칸 이동
                # 최단 경루가 여러개면 우, 하, 좌, 상 순서
                # 경로가 존재하지 않으면 제자리

        # 안식처 도착
            # 즉시 지도에서 제외되며 해당 턴을 도착 시간으로 기록
        
        # 참고: 해저 화산이 있는 칸으로 진입할 수 있고, 앞선 거북이의 결과는 즉시 다음 거북이의 경로 탐색에 반영

    # 2단계: 화산 압력 증가
        # 바다에 존재하는 모든 해저 화산의 마그마 압력이 10씩 증가

    # 3단계: 화산 분출 및 연쇄 반응
        # 현재 마그마 압력이 각 화산의 임계치 이상인 화산은 열기를 분출

        # 1. 열기 전파:
            # 화산이 위치한 칸에 분출 임계치(P) 만큼의 열기가 발생
            # 열기는 상하좌우로 뻗어나가며 한 칸 이동할 때 마다 열기의 절반(소수점 내림)을 전파
            # 산호초를 만나거나 열기 값이 0이 되면 전파 중단
            # 한 칸에 여러 열기가 도달하면 합산

        # 2. 연쇄 반응:
            # 아직 분출하지 않은 화산 중, (현재 마그마 압력 + 해당 칸에 누적된 외부 열기) >= P가 되면 해당 화산도 즉시 분출
            # 외부 열기는 분출 조건만 만족시킬 뿐, 해당 화산의 실제 마그마 압력 수치 자체를 증가시키지는 않음
            # 새로 분출하는 화산이 없을 때 까지 반복

        # 3. 바다거북의 위기(화석화)
            # 모든 분출이 종료된 후, 살아있는 거북이가 위치한 칸의 총 열기 합이 20이상이면 해당 거북이는 화석이 됨
            # 화석이 된 거북이는 그 자리에 고정되어, 이후 턴부터 다른 거북이를 방해하는 장애물이됨

    # 4단계: 바다 환경 초기화
        # 바다 위의 모든 열기 정보는 사라짐
        # 이번 턴에 분출을 일으킨 모든 화산(연쇄 반응 포함)의 마그마 압력은 0으로 초기화
        # 분출하지 않은 화산의 압력은 그대로 유지

# 바다거북이 안식처에 도착한 턴 번호 출력
# 100턴 내에 도착하지 못했거나 도중에 화석이 되었다면 -1 출력

import sys
from collections import deque

input = sys.stdin.readline


def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-----')


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def pressure_improve(p_arr, volcano):
    for i, j, _, _ in volcano:
        p_arr[i][j] += 10
    return p_arr

def search(ti, tj):
    q = deque([[ti, tj]])
    #
    v = [[0] * N for _ in range(N)]
    backtrack = [[None] * N for _ in range(N)]
    v[ti][tj] = 1
    #
    found = False
    while q:
        ci, cj = q.popleft()
        if (ci, cj) == (N - 1, N - 1):
            found = True

        #
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and (t_arr[ni][nj] != 1 and t_arr[ni][nj] != -2 and t_arr[ni][nj] != -1) and not v[ni][nj]:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
                backtrack[ni][nj] = [ci, cj]

    if not found:
        return -1  # 경로가 없는 경우

    path = []
    curr = (N - 1, N - 1)
    while curr is not None:
        path.append(curr)
        curr = backtrack[curr[0]][curr[1]]

    path.reverse()  # 시작 -> 도착 순서로 뒤집기
    return path[1]

def spread(v_arr, i, j, P, coords):
    v = [[0] * N for _ in range(N)]
    coords.append([i, j])
    # 열기 확산
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        cnt = 0
        ci, cj = i, j
        for _ in range(N):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and t_arr[ni][nj] != 1:
                v[ni][nj] = 1
                cnt += 1
                v_arr[ni][nj] += P // (2 ** cnt)
                ci, cj = ni, nj
                coords.append([ni, nj])

    return v_arr, coords

def active_volcano(p_arr, volcano):
    lst = []
    coords = []
    for idx, (i, j, P, status) in enumerate(volcano):
        # 마그마 압력으로만 폭발하는 화산이 있는지 확인
        if status == 0 and p_arr[i][j] >= P:
            lst.append([idx, i, j, P])

    # 화산 열기 관리 arr : 화산 압력 및 열기 관리
    v_arr = [x[:] for x in arr]

    # 마그마 압력으로만 폭발
    for idx, i, j, P in lst:
        # 열기 확산
        v_arr[i][j] = P
        v_arr, coords = spread(v_arr, i, j, P, coords)
        volcano[idx][-1] = 1

    # 연쇄 작용 확인
    while True:
        valid = False
        for idx, (i, j, P, status) in enumerate(volcano):
            if status == 0 and v_arr[i][j]+p_arr[i][j] >= P:
                #
                v_arr[i][j] = P
                # 열기 확산
                v_arr, coords = spread(v_arr, i, j, P, coords)
                volcano[idx][-1] = 1
                #
                valid = True
        if not valid:
            break

    return v_arr, coords


N, M, K = map(int, input().strip().split())  # N: 격자 크기 / M: 거북 수 / K: 화산 수
arr = [list(map(int, input().strip().split())) for _ in range(N)]
turtle = [list(map(int, input().strip().split())) for _ in range(M)]
i_volcano = [list(map(int, input().strip().split())) for _ in range(K)]
answer = []
TURN = 100

# turtles 배열에 거북이 id 추가
turtles = []
for idx, (i, j) in enumerate(turtle):
    turtles.append([idx + 1, i, j])

# 화산 폭발 상태 추가
volcano = []
for idx, (i, j, P) in enumerate(i_volcano):
    volcano.append([i, j, P, 0])

# 거북이 관리 arr
t_arr = [x[:] for x in arr]
for id, i, j in turtles:
    t_arr[i][j] = -1
# print_map(t_arr)

# 화산 압력 관리 arr
p_arr = [x[:] for x in arr]

for t in range(TURN):
    # 1단계: 바다 거북 이동
    for idx, (id, ti, tj) in enumerate(turtles):
        if t_arr[ti][tj] != -2 and (ti, tj) != (N-1, N-1):
            if search(ti, tj) == -1:  # -1이면 경로 없다는 거
                continue
            else:  # 경로가 있는 경우
                # 한 칸 이동한 위치로 갱신
                ei, ej = search(ti, tj)
                t_arr[ti][tj] = 0
                t_arr[ei][ej] = -1
                ti, tj = ei, ej
                turtles[idx] = [id, ti, tj]
                if (ti, tj) == (N - 1, N - 1):  # 안식처 도착하면
                    answer.append([id, t+1])  # 도착 시간 기록

                    # 지도에서 제거
                    t_arr[ti][tj] = 0

    # print_map(t_arr)

    # 2단계: 화산 압력 증가
    p_arr = pressure_improve(p_arr, volcano)
    # print_map(p_arr)

    # 3단계: 화산 분출 및 연쇄 반응
    active = False
    for idx, (i, j, P, status) in enumerate(volcano):
        # 마그마 압력으로만 폭발하는 화산이 있는지 확인
        if status == 0 and p_arr[i][j] >= P:
            active = True

    if active:
        v_arr, coords = active_volcano(p_arr, volcano)
        # print_map(v_arr)
        # print(coords)

        # 화석화
        for idx, (id, ti, tj) in enumerate(turtles):
            if [ti, tj] in coords and v_arr[ti][tj] >= 20 and t_arr[ti][tj] == -1:
                t_arr[ti][tj] = -2
                answer.append([id, -1])

        # 4단계: 바다 환경 초기화
        v_arr = [x[:] for x in arr] # 바다 위의 모든 열기 정보는 사라짐
        p_arr_bk = [x[:] for x in arr]
        for idx, (i, j, P, status) in enumerate(volcano):
            if status == 0:
                p_arr_bk[i][j] = p_arr[i][j] # 분출하지 않은 화산의 압력은 유지
            if status == 1:
                volcano[idx][-1] = 0

        p_arr = p_arr_bk
        # print_map(v_arr)

for idx, (id, ti, tj) in enumerate(turtles):
    if t_arr[ti][tj] == -1:
        answer.append([id, -1])

answer.sort(key=lambda x: x[0])
for id, time in answer:
    print(time)

