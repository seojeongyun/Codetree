# 격자: N x N
    # (0, 0)부터 (N-1,N-1)
    # 0: 도로
    # 1: 도로가 아닌 곳

# 메두사의 이동
    # 집부터 공원까지 이동
        # 집: Sr, Sc
        # 공원: Er, Ec

    # 오직 도로만을 따라 최단 경로로 공원까지 이동

# 용감한 전사
    # M명
    # ri, ci에 위치해있으며, 메두사를 향해 최단 경로로 이동
    # 도로와 비도로를 구분하지 않고 어느 칸이든 이동 가능

# [1] 메두사의 이동
    # 공원까지의 최단 경로 중 도로를 따라 한 칸 이동
        # 최단 경로가 여러개라면 상하좌우의 우선순위를 따름
        # 집부터 공원까지 도달하는 경로가 없을 수도 있다. (정답에 -1 리턴)
    # 메두사가 이동한 칸에 전사가 있을 경우 전사는 사라진다.

# [2] 메두사의 시선
    # 메두사는 상하좌우 중 하나의 방향을 선택해 바라봄
        # 상하좌우 중 전사를 가장 많이 볼 수 있는 방향을 봄
        # 전사 수가 같다면 상하좌우 우선순위
    # 바라보는 방향으로 90도의 시야 각을 가짐
        # 현재 턴에 움직일 수 없고, 이번 턴이 종료되었을 때 돌에서 풀려남
        # 두 명 이상의 전사가 같은 칸에 위치하면 둘 다 돌로 변함

# [3] 전사들의 이동
    # 돌로 변하지 않은 전사는 메두사를 향해 최대 2칸 이동
    # 첫 번째 이동
        # 메두사와 거리를 줄일 수 있는 방향으로 한 칸
            # 여러개면 상하좌우 우선순위
        # 격자 밖이랑 메두사의 시야에 들어오는 곳으로 이동 불가능

    # 두 번째 이동
        # 메두사와 거리를 줄이를 수 있는 방향으로 한 칸 더 이동
            # 좌우상하의 우선순위
        # 격자 밖이랑 메두사의 시야에 들어오는 곳으로 이동 불가능

# [4] 전사의 공격
    # 메두사와 같은 칸에 도달한 전사는 사라짐

# 위의 네 단계에서 최단 경로 계산은 맨해튼 거리를 기준으로

# 출력: 위의 네 단계가 반복되어 메두사가 공원에 도달할 때 까지 매 턴마다 해당 턴에서
    # 모든 전사가 이동한 거리의 합
    # 메두사로 인해 돌이 된 전사의 수
    # 메두사를 공격한 전사의 수를 공백을 사이에 두고 차례대로 출력

    # 메두사가 공원에 도착하는 턴에는 0을 출력하고 프로그램 종료

from collections import deque

# ----------------------------------
def myprint(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('-------------------')
# ----------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N
# ----------------------------------
def check_home_to_park(si, sj, ei, ej):
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    q = deque([[si, sj]])

    while q:
        ci, cj = q.popleft()
        # 종료 조건
        if (ci, cj) == (ei, ej):
            return True

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not visited[ni][nj] and not arr[ni][nj]:
                q.append([ni, nj])
                visited[ni][nj] = 1

    return False
# ----------------------------------
def get_manhattan(i,j,k,l):
    return abs(i-k) + abs(j-l)
# ----------------------------------
def get_dist(si, sj, ei, ej):
    visited = [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    q = deque([[si, sj]])

    while q:
        ci, cj = q.popleft()
        # 종료 조건
        if (ci, cj) == (ei, ej):
            return visited[ci][cj] - 1

        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not visited[ni][nj] and arr[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = visited[ci][cj] + 1
# ----------------------------------
def move_medusa(si, sj, ei, ej):
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = si + di, sj + dj
        if in_range(ni, nj) and get_dist(si, sj, ei, ej) > get_dist(ni, nj, ei, ej) and not arr[ni][nj]:
            arr[si][sj] = 0
            arr[ni][nj] = 2
            # ni, nj에 전사가 있다면,
            if w_arr[ni][nj] > 0:
                for idx, (i, j, stone, live) in enumerate(warriors):
                    if live == 0: continue
                    if (i, j) == (ni, nj):
                        warriors[idx][3] = 0

                    w_arr[ni][nj] = 0
            return ni, nj
# ----------------------------------
def forward(coords, si, sj, dir_num, trig):
    if trig == 0:
        if in_range(si, sj):
            coords.add((si, sj))
        if in_range(si, sj) and w_arr[si][sj] > 0:
            return coords, si, sj

        while True:
            ni, nj = si + dis[dir_num], sj + djs[dir_num]
            if in_range(ni, nj):
                coords.add((ni, nj))
                si, sj = ni, nj
                if w_arr[ni][nj] > 0:
                    return coords, ni, nj
            else:
                return coords, -1, -1

    else:
        while True:
            ni, nj = si + dis[dir_num], sj + djs[dir_num]
            if in_range(ni, nj):
                coords.add((ni, nj))
                si, sj = ni, nj
            elif not in_range(ni, nj):
                break
        return coords, ni, nj
# ----------------------------------
def find_end_point(coords, si, sj, di, dj):
    cnt = 0
    while True:
        ni, nj = si + di, sj + dj
        if in_range(ni, nj) and w_arr[ni][nj] == 0:
            cnt += 1
            coords.add((ni, nj))
            si, sj = ni, nj
        else:
            if not in_range(ni, nj):
                return coords, cnt, -1, -1
            elif w_arr[ni][nj] > 0:
                coords.add((ni, nj))
                return coords, cnt+1, ni, nj
# ----------------------------------
def get_view(si, sj): # 바라보는 방향 및 좌표 획득
    # 전사가 가장 많은 방향 바라보기 + 동률이면 상하좌우 우선순위
    max_seen = -1
    max_coords = set()
    max_seen_warriors = set()

    for dir_num in (3, 1, 2, 0):
        coords = set()
        # 대각 방향을 처리해서 si, sj를 넘겨줘야함.
        left, right = diagonal[dir_num]

        # 왼쪽 대각선 탐색
        left_di, left_dj = left
        coords, left_cnt, wi, wj = find_end_point(coords, si, sj, left_di, left_dj)

        # 오른쪽 대각선 탐색
        right_di, right_dj = right
        coords, right_cnt, wi, wj = find_end_point(coords, si, sj, right_di, right_dj)

        # 왼쪽 대각에서 직진 탐색
        for i in range(left_cnt):
            lsi = si + left_di * (i + 1)
            lsj = sj + left_dj * (i + 1)
            coords, wi, wj = forward(coords, lsi, lsj, dir_num, 0)

        # 오른쪽 대각에서 직진 탐색
        for i in range(right_cnt):
            rsi = si + right_di * (i + 1)
            rsj = sj + right_dj * (i + 1)
            coords, wi, wj = forward(coords, rsi, rsj, dir_num, 0)

        # 중앙 탐색
        coords, wi, wj = forward(coords, si+dis[dir_num], sj+djs[dir_num], dir_num, 0)

        # 병사에 의해 가려지는 좌표 계산
        occlusion_coords = set()
        view = coords
        for wi, wj in coords:
            if w_arr[wi][wj] > 0:
                if dir_num == 0: # 오른쪽 볼 때
                    if wi < si: # 왼쪽 탐색 및 포워드
                        # 왼쪽 대각선 탐색
                        occlusion_coords, left_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, left_di, left_dj)
                        # 왼쪽 대각에서 직진 탐색
                        for i in range(left_cnt):
                            lsi = wi + left_di * (i + 1)
                            lsj = wj + left_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, lsi, lsj, dir_num, 1)

                    elif wi > si: # 오른쪽 탐색 및 포워드
                        # 오른쪽 대각선 탐색
                        occlusion_coords, right_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, right_di, right_dj)
                        # 오른쪽 대각에서 직진 탐색
                        for i in range(right_cnt):
                            rsi = wi + right_di * (i + 1)
                            rsj = wj + right_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, rsi, rsj, dir_num, 1)

                elif dir_num == 1:
                    if wj > sj: # 왼쪽
                        # 왼쪽 대각선 탐색
                        occlusion_coords, left_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, left_di, left_dj)
                        # 왼쪽 대각에서 직진 탐색
                        for i in range(left_cnt):
                            lsi = wi + left_di * (i + 1)
                            lsj = wj + left_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, lsi, lsj, dir_num, 1)

                    elif wj < sj: # 오른쪽
                        # 오른쪽 대각선 탐색
                        occlusion_coords, right_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, right_di, right_dj)
                        # 오른쪽 대각에서 직진 탐색
                        for i in range(right_cnt):
                            rsi = wi + right_di * (i + 1)
                            rsj = wj + right_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, rsi, rsj, dir_num, 1)

                elif dir_num == 2:
                    if wi > si: # 왼쪽
                        # 왼쪽 대각선 탐색
                        occlusion_coords, left_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, left_di, left_dj)
                        # 왼쪽 대각에서 직진 탐색
                        for i in range(left_cnt):
                            lsi = wi + left_di * (i + 1)
                            lsj = wj + left_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, lsi, lsj, dir_num, 1)

                    elif wi < si: # 오른쪽
                        # 오른쪽 대각선 탐색
                        occlusion_coords, right_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, right_di, right_dj)
                        # 오른쪽 대각에서 직진 탐색
                        for i in range(right_cnt):
                            rsi = wi + right_di * (i + 1)
                            rsj = wj + right_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, rsi, rsj, dir_num, 1)

                elif dir_num == 3:
                    if wj < sj: # 왼쪽
                        # 왼쪽 대각선 탐색
                        occlusion_coords, left_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, left_di, left_dj)
                        # 왼쪽 대각에서 직진 탐색
                        for i in range(left_cnt):
                            lsi = wi + left_di * (i + 1)
                            lsj = wj + left_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, lsi, lsj, dir_num, 1)

                    elif wj > sj: # 오른쪽
                        # 오른쪽 대각선 탐색
                        occlusion_coords, right_cnt, _, _ = find_end_point(occlusion_coords, wi, wj, right_di, right_dj)
                        # 오른쪽 대각에서 직진 탐색
                        for i in range(right_cnt):
                            rsi = wi + right_di * (i + 1)
                            rsj = wj + right_dj * (i + 1)
                            occlusion_coords, _, _ = forward(occlusion_coords, rsi, rsj, dir_num, 1)
                # 직진
                occlusion_coords, _, _ = forward(occlusion_coords, wi + dis[dir_num], wj + djs[dir_num], dir_num, 1)
                #
                view = coords - occlusion_coords

        # 보이는 병사 수 세기
        seen_set = set()
        seen_num = 0
        for i, j in view:
            if w_arr[i][j] > 0:
                seen_num += w_arr[i][j]
                seen_set.add((i, j))

        if max_seen < seen_num:
            max_seen = seen_num
            max_coords = view
            max_seen_warriors = seen_set
            #
    return max_coords, max_seen_warriors
# ----------------------------------
def move_warriors(si, sj, warriors, view_coords):
    move_cnt = 0
    attack_cnt = 0
    for idx, (wi, wj, stone, live) in enumerate(warriors):
        if stone == 1 or live == 0:
            continue

        # 첫 번째 이동
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = wi + di, wj + dj
            if in_range(ni, nj) and get_manhattan(ni, nj, si, sj) < get_manhattan(wi, wj, si, sj) and (ni, nj) not in view_coords:
                move_cnt += 1
                if arr[ni][nj] == 2: # 메두사를 만나면
                    w_arr[wi][wj] -= 1
                    attack_cnt += 1
                    warriors[idx][3] = 0
                    break
                else:
                    w_arr[wi][wj] -= 1
                    w_arr[ni][nj] += 1
                    #
                    wi, wj = ni, nj
                    warriors[idx][0], warriors[idx][1] = wi, wj
                    break

    for idx, (wi, wj, stone, live) in enumerate(warriors):
        if stone == 1 or live == 0:
            continue

        # 두 번째 이동
        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ni, nj = wi + di, wj + dj
            if in_range(ni, nj) and get_manhattan(ni, nj, si, sj) < get_manhattan(wi, wj, si, sj) and (ni, nj) not in view_coords:
                move_cnt += 1
                if arr[ni][nj] == 2: # 메두사를 만나면
                    w_arr[wi][wj] -= 1
                    attack_cnt += 1
                    warriors[idx][3] = 0
                    break
                else:
                    w_arr[wi][wj] -= 1
                    w_arr[ni][nj] += 1
                    wi, wj = ni, nj
                    warriors[idx][0], warriors[idx][1] = wi, wj
                    break

    return move_cnt, attack_cnt

# ----------------------------------
N, M = map(int, input().split())
si, sj, ei, ej = map(int, input().split())
warrior_input = list(map(int, input().split()))
warriors = [] # [i, j, 돌 여부, 생존 여부]
cnt = 0
for _ in range(M):
    i, j = warrior_input[cnt*2:cnt*2+2]
    warriors.append([i, j, 0, 1])
    cnt+= 1

arr = [list(map(int, input().split())) for _ in range(N)]
arr[si][sj] = 2
w_arr = [[0] * N for _ in range(N)]

dis, djs = (0, 1, 0, -1), (1, 0, -1, 0)
diagonal = {
    #   왼쪽(i, j), 오른쪽(i, j)
    0: [(-1, 1), (1, 1)],  # 바라보는 방향 기준 Left(0), Right(1)에 대한 di, dj
    1: [(1, 1), (1, -1)],
    2: [(1, -1), (-1, -1)],
    3: [(-1, -1), (-1, 1)]
}


for i, j, _, _ in warriors:
    w_arr[i][j] = 1

# 집에서 공원까지 최단 거리가 존재하는가?
if check_home_to_park(si, sj, ei, ej):
    while True:
        answer = []
        # 돌로 변해있는 전사가 있다면 해제
        for idx, (i, j, stone, live) in enumerate(warriors):
            if warriors[idx][2] == 1:
                warriors[idx][2] = 0

        # [1] 메두사의 이동
        si, sj = move_medusa(si, sj, ei, ej)
        # myprint(arr)

        # [2] 메두사의 시선: 바라보는 방향 및 좌표 획득
        view_coords, seen_warriors = get_view(si, sj)

        # 보여진 전사는 돌로 변함
        stone_cnt = 0
        for idx, (i, j, stone, live) in enumerate(warriors):
            if (i, j) in seen_warriors and warriors[idx][3] == 1:
                stone_cnt += 1
                warriors[idx][2] = 1

        # [2]의 디버깅
        view_arr = [[0] * N for _ in range(N)]  # debug arr
        for i, j in view_coords:
            view_arr[i][j] = 1
        # myprint(view_arr)

        # [3] 전사들의 이동
        move_cnt, attack_cnt = move_warriors(si, sj, warriors, view_coords)

        # 종료 조건: 메두사가 공원에 도착 했는가?
        if (si, sj) == (ei, ej):
            print(0)
            break

        else:
            # myprint(w_arr)
            answer.append(move_cnt)
            answer.append(stone_cnt)
            answer.append(attack_cnt)

        print(*answer)
else:
    print(-1)


'''
new_arr = [[0] * N for _ in range(N)]
for i, j in view_coords:
    new_arr[i][j] = 1
myprint(new_arr)
'''