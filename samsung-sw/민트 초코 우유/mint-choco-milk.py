# 격자: N x N
    # 1행 1열부터 N행 N열까지

# 학생
    # 격자의 각 칸에 학생 존재, 총 N*N 명

    # 각 학생은 민트(T), 초코(C), 우유(M) 중 하나의 음식만을 신봉, F_(i, j)로 주어짐
    # 초기에는 하나만 신봉하지만 다른 사람에게 영향을 받아 초코우유, 민트우유, 민트초코, 민트초코우유를 신봉하는 학생이 생길 수도 있음

    # 각 학생은 초기 신앙심을 가지고 있으며 B_(i,j)로 주어짐
    # 하루: 아침, 점심, 저녁 순서이고 T일 진행

# 하루
    # 아침
        # 각 학생은 신앙심을 1씩 얻음.

    # 점심
        # 인접한 학생들과 신봉 음식이 완전히 같은 경우 그룹 형성
            # 인접 위치: 상하좌우로 붙어있는
        # 그룹 내 대표자 선정
            # 기준: 그룹 내 신앙심이 가장 큰 사람 -> rk가 작은 -> ck가 작은
            # rk, ck는 그룹 내 후보 학생들의 좌표를 의미
        # 대표자를 제외한 그룹원들은 각자 신앙심을 1씩 대표자에게 넘김
            # 대표자의 신앙심은 그룹원 수-1 만큼 추가되고 나머지 그룹원은 1씩 감소

    # 저녁
        # 모든 그룹의 대표자들이 신앙을 전파
            # 신앙심 B중 1만 남기고 나머지를 간절함(x=B-1)로 바꿔 전파에 사용
            # 전파 방향은 B를 4로 나눈 나머지에 따라 결정
                # 나머지가 0, 1, 2, 3인 경우 각 순서대로 위, 아래, 왼, 오
            # 전파할 방향으로 한 칸 씩 이동하며 전파 시도
                # 격자 밖으로 나가거나 간절함이 0이되면 전파 종료
            # 전파 대상이 전파자의 신봉 음식과 완전히 같으면, 전파를 하지 않고 다음으로 넘어감
            # 신봉 음식이 다른 경우, 전파 진행.
                # 강한 전파: 전파 대상의 신앙심을 y라 할 때 x > y면 전파에 성공
                    # 전파 대상은 전파자의 신봉 음식과 동일한 음식을 신봉하게 됨
                    # 전파자는 간절함이 (y+1)만큼 깎이며, 전파 대상의 신앙심은 1 증가
                    # 이 때 전파자의 간절함이 0이 된다면 더 이상 전파를 진행하지 않고 종료
                # 약한 전파: x <= y이면 약한 전파에 성공
                    # 전파 대상은 기존에 관심을 가지고 있던 기본 음식과 전파자가 관심을 갖는 기본 음식을 모두 합친 음식을 신봉
                    # 전파자는 간절함이 0이 되고 전파 종료, 전파 대상의 신앙심은 x만큼 증가
                # 어떤 학생이 다른 음식의 대표자에게 전파를 당했다면, 해당 학생은 당일에는 전파를 하지 않음. 전파를 받는 건 가능.
        # 전파 순서
            # 음식 기준
                # 단일 음식 - 민트, 초코, 우유
                # 이중 조합 - 초코우유, 민트우유, 민트초코
                # 삼중 조합 - 민트초코우유
            # 같은 그룹 내에서는
                # 대표자의 신앙심이 높은 순 -> 대표자의 행번호가 작은 순 -> 대표자의 열번호가 작은 순

# 각 날의 저녁 시간이 끝난 후, 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트 순서대로 각 음식의 신봉자들의 신앙심 총합을 출력
# -----------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N
# -----------------------------------
def food_arr_input():
    # 민트(T), 초코(C), 우유(M)
    food_dict = {
        'T': 1,
        'C': 2,
        'M': 4
    }

    food_arr = [[0] * N for _ in range(N)]

    for i in range(N):
        food_lst = input()
        for j, f in enumerate(food_lst):
            food_arr[i][j] = food_dict[f]


    return food_arr
# -----------------------------------
def believe_arr_input():
    arr = [list(map(int, input().split())) for _ in range(N)]
    return arr
# -----------------------------------
def morning(b_arr):
    for i in range(N):
        for j in range(N):
            b_arr[i][j] += 1

    return b_arr
# -----------------------------------
def bfs(v, i, j):
    now_food = f_arr[i][j]
    candidate = [[b_arr[i][j], i, j]]
    v[i][j] = 1
    #
    q = deque([[i, j]])

    while q:
        ci, cj = q.popleft()
        #
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and f_arr[ni][nj] == now_food:
                q.append([ni, nj])
                v[ni][nj] = 1
                candidate.append([b_arr[ni][nj], ni, nj])

    return candidate
# -----------------------------------
def grouping(f_arr):
    # [음식, 좌표, 신앙심, 간절함(초기엔 0), 단일-이중-삼중] 정보를 return
    boss_lst = []
    group_lst = []
    v = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                candidate = bfs(v, i, j) # candidate는 [신앙심, i, j] 의 리스트틀로 구성
                candidate.sort(key=lambda x: (-x[0], x[1], x[2]))
                b, bi, bj = candidate[0]
                food = f_arr[bi][bj]
                if food in single:
                    group = -1
                elif food in double:
                    group = -2
                elif food in tri:
                    group = -3
                boss_lst.append([food, [bi, bj], b, 0, group])
                group_lst.append(candidate[1:])

    return boss_lst, group_lst
# -----------------------------------
def make_believe(b_arr, boss_lst, group_lst):
    # 대표자를 제외한 그룹원들은 각자 신앙심을 1씩 대표자에게 넘김
    for idx, (_, coords, _, _, _) in enumerate(boss_lst):
        bi, bj = coords
        for b, i, j in group_lst[idx]:
            b_arr[i][j] -= 1
        b_arr[bi][bj] += len(group_lst[idx])
        boss_lst[idx][2] = b_arr[bi][bj]
    return b_arr
# -----------------------------------
def spread(dir_num, food, coords, believe, please, group):
    block = []
    bi, bj = coords
    while True:
        ni, nj = bi + dis[dir_num], bj + djs[dir_num]

        # 종료 조건
        if not in_range(ni, nj) or please <= 0:
            break

        # 음식이 같으면 다음으로 넘어감
        if f_arr[ni][nj] == f_arr[bi][bj]:
            bi, bj = ni, nj
            continue

        # 강한 전파
        else:
            if please > b_arr[ni][nj]:
                f_arr[ni][nj] = food
                please -= (b_arr[ni][nj]+1)
                b_arr[ni][nj] += 1
                block.append([ni, nj])
            # 약한 전파
            elif please <= b_arr[ni][nj]:
                f_arr[ni][nj] = f_arr[ni][nj] | f_arr[bi][bj]
                b_arr[ni][nj] += please
                please = 0
                block.append([ni, nj])
            bi, bj = ni, nj

    return block
# -----------------------------------

# -----------------------------------

from collections import deque

N, T = map(int, input().split())
f_arr = food_arr_input()
b_arr = believe_arr_input()

# 그룹 세트
single = {1, 2, 4}
double = {3, 5, 6}
tri = {7}

# 방향
dis, djs = (-1, 1, 0, 0), (0, 0, -1, 1)

# T일 동안 진행
for _ in range(T):
    answer = []
    # [1] 아침: 각 학생은 신앙심을 1씩 얻음
    b_arr = morning(b_arr)

    # [2] 점심
    # 그룹 형성 및 대표자 리스트 생성
    boss_lst, group_lst = grouping(f_arr) # [음식, 좌표, 신앙심, 간절함(초기엔 0), 단일-이중-삼중] 정보를 return

    # 대표자를 제외한 그룹원들은 각자 신앙심을 1씩 대표자에게 넘김
    b_arr = make_believe(b_arr, boss_lst, group_lst)

    # [3] 저녁: 신앙을 전파
    # 대표자 리스트에서 우선순위 설정
    boss_lst.sort(key=lambda x: (-x[4], -x[2], x[1][0], x[1][1]))

    block_lst = []
    for food, coords, believe, please, group in boss_lst:
        if coords in block_lst:
            continue

        # 전파 방향 설정: 각 대표자의 신앙심 B를 4로 나눈 나머지
        dir_num = b_arr[coords[0]][coords[1]] % 4

        # 신앙심 B중 1만 남기고 나머지를 간절함으로 바꾼다.
        please = b_arr[coords[0]][coords[1]] - 1
        b_arr[coords[0]][coords[1]] = 1

        # 전파
        block_coords = spread(dir_num, food, coords, believe, please, group)
        if block_coords != []:
            for lst in block_coords:
                block_lst.append(lst)
    # 출력:
    for f in (7, 3, 5, 6, 4, 2, 1):
        sm = 0
        for i in range(N):
            for j in range(N):
                if f_arr[i][j] == f:
                    sm += b_arr[i][j]
        answer.append(sm)
    print(*answer)
# 각 날의 저녁 시간이 끝난 후, 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트 순서대로 각 음식의 신봉자들의 신앙심 총합을 출력

