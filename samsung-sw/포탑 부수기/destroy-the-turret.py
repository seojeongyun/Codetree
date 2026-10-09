from collections import deque


# 격자: N x M
# 모든 위치에 포탑 존재 (포탑 개수는 NM개)

# 포탑
# 각 포탑은 공격력 존재
# 상황에 따라 공격력이 늘거나 줄어들 수 있음
# 공격력이 0 이하가 되면 해당 포탑은 부서져 더이상 공격 불가
# 최초에 공격력이 0인 포탑 존재할 수 있음

# K턴
# 부서지지 않은 포탑이 1개가 되면 즉시 중지

# [1] 공격자 선정
# 부서지지 않은 포탑 중 가장 공격력이 낮은 포탑이 공격자 -> 공격력 N+M 증가
# 2개 이상이면 가장 최근에 공격한 포탑
# 2개 이상이면, 포탑 위치의 행+열 합이 가장 큰 포탑
# 2개 이상이면 포탑 위치의 열이 가장 큰 포탑

# [2] 공격
# 가장 공격력이 높은 포탑을 공격
# 2개 이상이라면, 공격한지 가장 오래된 포탑
# 2개 이상이라면 행과 열의 합이 가장 작은 포탑
# 2개 이상이라면 각 포탑 위치의 열이 가장 작은 포탑

# [2-1] 레이저 공격
# 공격 시 레이저 공격을 먼저 시도하고 그게 안되면 포탄 공격
# 상하좌우 4개 방향으로 이동 가능
# 부서진 포탑이 있는 위치는 지날 수 없음
# 가장 자리에서 막힌 방향으로 진행하고자 하면, 반대방향으로 나옴 (% 연산자 활용)

# 공격자의 위치에서 공격대상 포탑까지 최단경로로 공격
# 2개 이상이면 우하좌상 우선순위
# 최단 경로가 정해졌으면 공격 대상은 공격력만큼의 피해를 입히며, 피해를 입은 포탑은 해당 수치만큼 공격력이 줄어듬
# 레이저 경로에 있는 포탑도 공격을 받게 되는데, 이들은 공격자 공격력의 절반만큼 공격을 받음 (2로 나눈 몫)
# 그런 경로가 존재 하지 않으면 포탄 공격

# [2-2] 포탄 공격
# 공격 대상은 공격자 공격력만큼의 피해를 받음
# 주위 8개 방향에 있는 포탑도 피해를 입는데, 공격자 공격력 절반만큼 피해를 받음
# 공격자는 해당 공격에 영향을 받지 않음
# 포탄이 가장자리에 떨어졌다면 반대편 격자까지 피해를 받음 (% 연산자)

# [3] 포탑 부서짐
# 공격력이 0 이하가 된 포탑은 부서짐

# [4] 포탑 정비
# 부서지지 않은 포탑 중 공격과 무관했던 포탑은 공격력이 1씩 올라감
# 공격과 무관했다는 건 공격자도 아니고, 공격에 피해를 입지도 않았다는 뜻
# ---------------------------------
def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:4}' for x in row))
    print('-------------------')


# ---------------------------------
def is_end(arr):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1

    if cnt == 1:
        return True

    else:
        return False
# ---------------------------------
def bfs(ai, aj, ti, tj):
    q = deque([[ai, aj]])
    v = [[0] * M for _ in range(N)]
    v[ai][aj] = (ai, aj)
    #
    route = []
    while q:
        ci, cj = q.popleft()

        # 종료 조건 및 좌표 저장
        if (ci, cj) == (ti, tj):
            ci, cj = v[ci][cj]
            while (ci, cj) != (ai, aj):
                route.append([ci, cj])
                ci, cj = v[ci][cj]
            route.append([ti, tj])
            return route[::-1]

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            # 가장자리 좌표 처리
            if ni == N: ni = 0
            elif ni == -1: ni = N - 1

            if nj == M: nj = 0
            elif nj == -1: nj = M - 1

            if not v[ni][nj] and arr[ni][nj] > 0:
                q.append([ni, nj])
                v[ni][nj] = (ci, cj)

    # 여기까지 왔다면 최단경로 없음
    return -1


# ---------------------------------
# ---------------------------------

# 입력
N, M, K = map(int, input().split())  # N: 행 / M: 열 / K: 턴 수
arr = [list(map(int, input().split())) for _ in range(N)]

# tower list
tower = []
for i in range(N):
    for j in range(M):
        attack = arr[i][j]
        att_time = 0
        alive = 1 if attack > 0 else 0
        tower.append([i, j, attack, att_time, alive])

# K턴 시작
for turn in range(K):
    # attacked arr 초기화
    attacked_arr = [x[:] for x in arr]

    # 종료조건: 살아있는 포탑이 1개라면 break
    if is_end(arr):
        break

    # [1] 공격자 선정
    tower.sort(key=lambda x: (-x[-1], x[2], -x[3], -(x[0] + x[1]), -x[1]))
    ai, aj, a_attack, a_att_time, a_alive = tower[0]
    a_attack += (M + N)
    arr[ai][aj] = a_attack
    attacked_arr[ai][aj] = -1

    # [2] 공격 대상 선정: 공격자를 제외한
    tower.sort(key=lambda x: (-x[-1], -x[2], x[3], (x[0] + x[1]), x[1]))
    ti, tj, t_attack, t_att_time, t_alive = tower[0]
    if (ai, aj) == (ti, tj): # 만약 공격자와 공격대상자가 동일하다면, 그 다음 인덱스
        ti, tj, t_attack, t_att_time, t_alive = tower[1]

    # [3] 공격
    # [3-1] 레이저 공격 판정: ai, aj에서 ti, tj로 가는 최단거리가 존재하는가?
    route = bfs(ai, aj, ti, tj)
    if route != -1:  # -1이 아니라면 레이저 공격 가능
        # 레이저 공격
        for i, j in route:
            if (i, j) == (ti, tj):
                # 공격력 만큼: arr, attacked_arr, tower 모두 갱신
                arr[ti][tj] -= a_attack
                attacked_arr[ti][tj] = -1
                #
                for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
                    if (ci, cj) == (ti, tj):
                        tower[idx][2] -= a_attack
                        break
            else:
                # 공격력 절반 만큼: arr, attacked_arr, tower 모두 갱신
                arr[i][j] -= (a_attack // 2)
                attacked_arr[i][j] = -1
                #
                for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
                    if (ci, cj) == (i, j):
                        tower[idx][2] -= (a_attack // 2)
                        break

    else:  # -1이라면 포탄 공격
        # 포탄 공격: ti, tj는 공격력 만큼, arr, attacked_arr, tower 모두 갱신
        arr[ti][tj] -= a_attack
        attacked_arr[ti][tj] = -1
        for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
            if (ci, cj) == (ti, tj):
                tower[idx][2] -= a_attack
                break

        # 포탄 공격: 8방향
        for di, dj in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)):
            ni, nj = ti + di, tj + dj
            # 가장자리 좌표 처리
            if ni == N: ni = 0
            elif ni == -1: ni = N - 1

            if nj == M: nj = 0
            elif nj == -1: nj = M - 1

            if arr[ni][nj] > 0 and (ni, nj) != (ai, aj):
                # 공격력 // 2 만큼, arr, attacked_arr, tower 모두 갱신
                arr[ni][nj] -= (a_attack // 2)
                attacked_arr[ni][nj] = -1
                for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
                    if (ci, cj) == (ni, nj):
                        tower[idx][2] -= (a_attack // 2)
                        break

    # 공격자 정보 갱신: tower, arr, attacked_arr
    for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
        if (ci, cj) == (ai, aj):
            tower[idx][2] = a_attack
            tower[idx][3] = turn+1
            break

    # [3] 포탑 부서짐: arr, tower 갱신
    for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
        if attack <= 0:
            arr[ci][cj] = 0
            tower[idx][4] = 0
            attacked_arr[ci][cj] = 0

    # [4] 포탑 정비: attacked_arr > 0 이면 +=1, tower 갱신
    for i in range(N):
        for j in range(M):
            if attacked_arr[i][j] > 0:
                arr[i][j] += 1
                for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
                    if (ci, cj) == (i, j):
                        tower[idx][2] += 1
                        break

# K턴이 종료된 후 남아있는 포탑 중 가장 강한 포탑의 공격력을 출력
max_att = -1
for idx, (ci, cj, attack, att_time, alive) in enumerate(tower):
    max_att = max(max_att, attack)

print(max_att)

