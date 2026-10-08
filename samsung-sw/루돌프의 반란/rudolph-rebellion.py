# 격자: N x N
    # (1,1)부터 (N,N)

# 게임
    # M번의 턴: 각 턴마다 루돌프와 산타들이 한 번 씩 움직임

    # [1] 루돌프의 움직임
        # 가장 가까운+게임에서 탈락하지 않은 산타를 향해 1칸 돌진
            # 두 명 이상이라면 r큰 -> c큰
        # 8방향 이동가능

    # [2] 산타의 움직임
        # 1번부터 P번까지 순서대로 이동
        # 기절했거나 게임에서 탈락한 산타는 이동 불가
        # 산타는 루돌프에게 가까워지는 방향으로 1칸 이동
        # 다른 산타가 있는 칸이나 게임판 밖으로는 이동 불가
        # 이동할 수 있는 칸이 없다면 이동하지 않음
        # 이동할 수 있는 칸이 있더라도 루돌프로부터 가까워질 수 있는 방법이 없다면 이동하지 않음
        # 상하좌우 4방향 이동 가능하고, 가까워질 수 있는 방향이 여러개면 상우하좌 우선순위

    # [3] 충돌
        # 산타와 루돌프가 같은 칸에 있으면 충돌
        # 루돌프가 움직여서 충돌이 일어난 경우
            # 해당 산타는 C만큼의 점수를 얻게 됨
            # 동시에 산타는 루돌프가 이동해온 방향으로 C칸 밀려남
        # 산타가 움직여서 충돌이 일어난 경우
            # 해당 산타는 D만큼의 점수를 얻게 됨
            # 동시에 산타는 자신이 이동해온 반대 방향으로 D칸 밀려남
        # 밀려나는 것은 포물선 모양을 그리며 밀려나는 것 = 이동하는 도중에 충돌이 일어나지 않고 정확히 원하는 위치에 도달
        # 밀려난 위치가 게임판 밖이면 탈락
        # 밀려난 칸에 다른 산타가 있는 경우 상호작용 발생

    # [4] 상호작용
        # 충돌에 의해 밀려난 산타가 착지하는 칸에 다른 산타가 있으면, 그 산타는 1칸 해당 방향으로 밀려남
        # 그 옆에 산타가 있다면 연쇄적으로 1칸씩 밀려나는 것을 반복
        # 게임판 밖으로 밀려나오게 된 산타의 경우 게임에서 탈락

    # [5] 기절
        # 산타는 루돌프와의 충돌 후 기절
        # k턴에 충돌 -> k+1까지 기절 -> k+2부터 정상 상태
        # 기절한 산타는 움직일 수 없음. 충돌이나 상호작용으로 인해 밀려날 수는 있음
        # 루돌프는 기절한 산타를 돌진 대상으로 선택 가능

    # [6] 게임 종료
        # M번의 턴에 걸쳐 루돌프, 산타가 순서대로 움직인 후 게임 종료
        # P명의 산타가 모두 게임에서 탈락하면 즉시 게임 종료
        # 매 턴 이후 아직 탈락하지 않은 산타들에게 1점씩 추가로 부여

# 출력: 게임이 끝났을 때 각 산타가 얻은 최종 점수를 출력

# ------------------------------------
def print_map(arr):
    for row in arr:
        # print(*row)
        print(' '.join(f'{x:2}' for x in row))
    print('----------------')
# ------------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N
# ------------------------------------
def get_dist(i1, j1, i2, j2):
    return (i1-i2)**2 + (j1-j2)**2
# ------------------------------------
def move_r(ri, rj):
    r_dir = -1
    max_dist = N*N
    ci, cj = ri, rj
    lst = []
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        if live == 0: continue
        #
        si, sj, _ = coords

        # 산타와의 거리 측정
        dist = get_dist(si, sj, ri, rj)
        lst.append([dist, si, sj])

    # 거리 가깝고, 행 크고, 열 큰 순서로 정렬
    lst.sort(key=lambda x: (x[0], -x[1], -x[2]))
    _, ti, tj = lst[0]
    dist = get_dist(ti, tj, ri, rj)
    # 8방향 중 target 위치로 가까워지는 방향으로 돌진
    if ti == ri:
        for dir, di, dj in ((0, 0, 1), (4, 0, -1)):
            n_ri, n_rj = ri + di, rj + dj
            if in_range(n_ri, n_rj):
                moved_dist = get_dist(ti, tj, n_ri, n_rj)
                if dist > moved_dist:
                    dist = moved_dist
                    r_dir, i, j = dir, n_ri, n_rj

    elif tj == rj:
        for dir, di, dj in ((2, 1, 0), (6, -1, 0)):
            n_ri, n_rj = ri + di, rj + dj
            if in_range(n_ri, n_rj):
                moved_dist = get_dist(ti, tj, n_ri, n_rj)
                if dist > moved_dist:
                    dist = moved_dist
                    r_dir, i, j = dir, n_ri, n_rj

    else:
        for dir, di, dj in ((7, -1, 1), (1, 1, 1), (3, 1, -1), (5, -1, -1)):
            n_ri, n_rj = ri + di, rj + dj
            if in_range(n_ri, n_rj):
                moved_dist = get_dist(ti, tj, n_ri, n_rj)
                if dist > moved_dist:
                    dist = moved_dist
                    r_dir, i, j = dir, n_ri, n_rj

    r_arr[ci][cj] = 0
    r_arr[i][j] = -1

    if s_arr[i][j] > 0:
        # 산타 기절, 이동, 점수
        attack_r(i, j, turn, r_dir, s_to_r=0)

    return r_dir, i, j
# ------------------------------------
def recursive(s_num, i, j, dir):
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        if live == 0: continue
        #
        si, sj, _ = coords
        if (si, sj) == (i, j) and idx != s_num:
            n_si, n_sj = si + dis[dir], sj + djs[dir]
            if not in_range(n_si, n_sj): # 격자 밖이면 게임 탈락
                s_arr[si][sj] = 0
                santa[idx][-1] = 0

            else:
                santa[idx][1] = [n_si, n_sj, dir]
                if s_arr[n_si][n_sj] > 0:  # 다른 산타가 있으면
                    recursive(idx, n_si, n_sj, dir)

                s_arr[si][sj] = 0
                s_arr[n_si][n_sj] = num
        # break
# ------------------------------------
def attack_r(ri, rj, turn, r_dir, s_to_r):
    value = D if s_to_r else C
    # 산타 기절, 이동, 점수
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        if live == 0: continue
        #
        si, sj, s_dir = coords
        if (si, sj) == (ri, rj):
            # 루돌프 혹은 산타의 힘에 의해 밀려난 위치
            dir = (s_dir - 4 + 8) % 8 if s_to_r else r_dir
            n_si, n_sj = si + (value * dis[dir]), sj + (value * djs[dir])
            if not in_range(n_si, n_sj): # 격자 밖이면 게임 탈락
                s_arr[si][sj] = 0
                santa[idx][-1] = 0
                santa[idx][3] += value

            else:   # 격자 안이면, 기절, 이동, 점수
                santa[idx][1] = [n_si, n_sj, dir]
                santa[idx][2] = [1, turn, turn+2]
                santa[idx][3] += value

                # 이동
                if s_arr[n_si][n_sj] > 0: # 다른 산타가 있으면
                    # 상호작용
                    recursive(idx, n_si, n_sj, dir)
                s_arr[si][sj] = 0
                s_arr[n_si][n_sj] = num
            break
# ------------------------------------
def move_s(ri, rj, r_dir):
    is_crash = False
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        mi, mj = -1, -1
        is_stun, start, end = stun
        if is_stun == 1 or live == 0: continue # 죽었거나, 기절이면 무시
        #
        si, sj, s_dir = coords
        dist = get_dist(ri, rj, si, sj)
        for dir, di, dj in ((6, -1, 0), (0, 0, 1), (2, 1, 0), (4, 0, -1)):
            ni, nj = si + di, sj + dj
            if in_range(ni, nj) and not s_arr[ni][nj]:
                moved_dist = get_dist(ri, rj, ni, nj)
                if dist > moved_dist:
                    dist = moved_dist
                    # 여기 왔다는 건 이동했다는 의미이므로 arr 및 리스트 갱신
                    santa[idx][1] = [ni, nj, dir]
                    mi, mj = ni, nj

                    # 충돌이 발생했나 ?
                    if r_arr[ni][nj] == -1:
                        is_crash = True
        if (mi, mj) != (-1, -1):
            s_arr[si][sj] = 0
            s_arr[mi][mj] = num

        if is_crash:
            # [4] 루돌프의 공격: 산타가 움직여 충돌이 발생한 경우
            attack_r(ri, rj, turn, r_dir, s_to_r=1)
# ------------------------------------
# ------------------------------------

# N: 격자 크기, M: 게임 턴 수, P: 산타의 수, C: 루돌프의 힘, D: 산타의 힘
N, M, P, C, D = map(int, input().split())
ri, rj = map(int, input().split())
ri, rj = ri-1, rj-1
s_lst = [list(map(int, input().split())) for _ in range(P)]

# 산타 리스트 재 작성: [[si, sj], [기절 여부, 기절 시작, 기절 시작 + 2], 점수, 생존]
santa = []
for idx, si, sj in s_lst:
    coords = [si-1, sj-1, -1]
    stun = [0, -1, -1]
    score = 0
    live = 1
    santa.append([idx, coords, stun, score, live])

# 8방향 dis, djs, 동쪽부터 시계방향
dis, djs = (0, 1, 1, 1, 0, -1, -1, -1), (1, 1, 0, -1, -1, -1, 0, 1)

# 산타 arr, 루돌프 arr
s_arr = [[0] * N for _ in range(N)]
r_arr = [[0] * N for _ in range(N)]
r_arr[ri][rj] = -1

for idx, (num, coords, stun, score, live) in enumerate(santa):
    si, sj, _ = coords
    s_arr[si][sj] = num


# 게임 시작
for turn in range(M):
    santa.sort(key=lambda x: x[0])
    # 해당 턴에 기절이 풀리는 산타가 있는지 확인하고 기절 풀기
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        is_stun, start, end = stun
        if turn == end:
            santa[idx][2] = [0, -1, -1]

    # [1] 루돌프의 이동: 탈락하지 않은 산타중 가장 가까운 방향으로
    r_dir, ri, rj = move_r(ri, rj)
    # print_map(r_arr)


    # [3] 산타의 움직임
    is_crash = move_s(ri, rj, r_dir)

    # 턴 종료시 살아남은 산타에게 1점 추가
    for idx, (num, coords, stun, score, live) in enumerate(santa):
        if live:
            santa[idx][3] += 1

    # [5] 게임 종료 확인: 모든 산타가 탈락했는가?
    out_cnt = 0
    for i in range(len(santa)):
        if santa[i][-1] == 0:
            out_cnt += 1
    if out_cnt == P:
        break

for i in range(len(santa)):
    print(santa[i][-2], end=' ')

























