from collections import deque


# 격자 : N x N
# (0,0) ~ (N-1, N-1)
# 산호초 (1), 다른 거북(-1 ~ -N), 화석(2)

# 시뮬레이션
# 최대 100턴

# [1] 바다거북 이동
# ID가 작은 순서대로 한 마리씩 이동
# 각 차례에 현재 바다 상태를 기준으로 (N-1, N-1)까지 최단 경로 탐색
# 최단 경로가 존재하면 해당 경로의 첫 번째 칸으로 이동
# 여러개라면 우 하 좌 상 순서로
# 최단 경로가 존재하지 않으면 제자리에 머묾
# 산호초, 다른 거북, 화석은 이동 불가
# (N-1, N-1) 도착하면 즉시 제외, 해당 턴을 도착 시간으로 기록

# [2] 화산 압력 증가
# 바다에 존재하는 모든 해저 화산의 마그마 압력이 각각 10씩 증가

# [3] 화산 분출 및 연쇄 반응
# 현재 마그마 압력이 각 화산의 분출 임계치(P) 이상이면 열기 분출
# [1] 열기 전파
# 화산이 위치한 칸에 해당 화산의 P만큼의 열기 발생
# 열기는 상하좌우 4 방향으로 뻗어나가며 한 칸 이동할 때 마다 열기//2
# 산호초를 만나거나 열기 값이 0이 되면 전파 중단
# 한 칸에 여러 화산의 열기가 도달하면 그 값을 모두 합산

# [2] 연쇄 반응
# 아직 분출하지 않은 화산 중 (현재 마그마 압력 + 외부 열기) >= P면 해당 화산도 분출 시작
# 외부 열기는 조건만 만족시킬 뿐, 해당 화산의 실제 마그마 압력 수치를 증가시키지는 않음
# 새로 분출하는 화산이 없을 때 까지 반복

# [3] 화석화
# 분출 종료 후, 살아있는 거북이가 위치한 칸의 열기 합이 20 이상이면 거북이 화석화

# [4] 환경 초기화
# 모든 열기 정보 사라짐
# 분출을 일으킨 화산의 마그마 압력 0으로 초기화
# 분출하지 않은 화산의 압력은 유지

# --------------------------
def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('----------------')


# --------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


# --------------------------
def bfs(i, j):
    q = deque([[i, j]])
    v = [[0] * N for _ in range(N)]
    v[i][j] = (i, j)
    route = []
    while q:
        ci, cj = q.popleft()
        #
        if (ci, cj) == (N - 1, N - 1):
            ci, cj = v[ci][cj]
            route.append([N - 1, N - 1])
            while (ci, cj) != (i, j):
                route.append([ci, cj])
                ci, cj = v[ci][cj]
            return route[::-1]
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and not arr[ni][nj]:
                q.append([ni, nj])
                v[ni][nj] = (ci, cj)
    return -1


# --------------------------
# --------------------------
# --------------------------
N, M, K = map(int, input().split())  # N : 격자 크기 / M : 거북이 수 / K : 화산 수
arr = [list(map(int, input().split())) for _ in range(N)]
turtles = [list(map(int, input().split())) for _ in range(M)]
volcanos = [list(map(int, input().split())) for _ in range(K)]

# 거북이는 arr에 표시, 압력 arr, 열기 arr 별도로
for idx, (ti, tj) in enumerate(turtles):
    arr[ti][tj] = -(idx + 1)
    turtles[idx] = [ti, tj, 0]  # i, j, 도착시간
p_arr = [[0] * N for _ in range(N)]
h_arr = [[0] * N for _ in range(N)]

# 시뮬레이션 시작
for time in range(1, 101):
    # [1] 바다 거북 이동
    for idx, (ti, tj, _) in enumerate(turtles):
        if arr[ti][tj] != 2 and (ti, tj) != (N-1, N-1):
            # 최단 경로 탐색
            route = bfs(ti, tj)
            if route == -1: continue  # 최단 경로가 없다면 skip

            # 최단 경로가 있다면 한 칸 이동
            if tuple(route[0]) == (N - 1, N - 1):  # 한 칸 이동한 게 안식처라면, 정답 처리 및 지도에서 제외
                arr[ti][tj] = 0
                turtles[idx] = [N - 1, N - 1, time]

            else:  # 한 칸 이동한 게 안식처가 아니라면, turtles, arr 갱신
                arr[ti][tj] = 0
                ti, tj = route[0]
                arr[ti][tj] = -(idx + 1)
                turtles[idx] = [ti, tj, 0]

    # [2] 화산 압력 증가
    for i, j, P in volcanos:
        p_arr[i][j] += 10

    # [3] 화산 분출 및 연쇄 반응
    activated = set()
    # [3-1] 현재 마그마 압력이 P 이상인 화산이 있다면 열기 전파
    for i, j, P in volcanos:
        if p_arr[i][j] >= P:
            activated.add((i, j))
            h_arr[i][j] = P  # 화산이 위치한 칸에 해당 화산의 P만큼 열기 발생
            for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                ci, cj = i, j
                for length in range(1, N+1):
                    ni, nj = ci + di, cj + dj
                    if not in_range(ni, nj) or arr[ni][nj] == 1:
                        break
                    h_arr[ni][nj] += h_arr[i][j] // (2**length)
                    ci, cj = ni, nj

    # [3-2] 아직 분출하지 않은 화산 중 (현재 마그마 압력 + 외부 열기) >= P인게 있다면 분출
    # 새로 분출하는 화산이 없을 때 까지 반복
    for _ in range(len(volcanos)):
        for i, j, P in volcanos:
            if p_arr[i][j] + h_arr[i][j] >= P and (i, j) not in activated:
                out_heat = h_arr[i][j]
                activated.add((i, j))
                h_arr[i][j] = P
                # P 전파
                for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    ci, cj = i, j
                    for length in range(1, N+1):
                        ni, nj = ci + di, cj + dj
                        if not in_range(ni, nj) or arr[ni][nj] == 1:
                            break
                        h_arr[ni][nj] += h_arr[i][j] // (2**length)
                        ci, cj = ni, nj

                h_arr[i][j] += out_heat

    # [3-3] 화석화
    for idx, (ti, tj, _) in enumerate(turtles):
        if h_arr[ti][tj] >= 20:
            if arr[ti][tj] < 0:
                arr[ti][tj] = 2
                turtles[idx] = [ti, tj, -1]

    # [4] 환경 초기화
    h_arr = [[0] * N for _ in range(N)]

    for i, j in activated:
        p_arr[i][j] = 0

for _, _, time in turtles:
    if time == 0:
        print(-1)
    else:
        print(time)