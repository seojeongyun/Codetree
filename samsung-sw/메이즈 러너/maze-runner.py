# 미로 탈출 게임
# M명의 참가자

# 미로의 구성
# 격자: N x N, 좌상단 (1,1)

# 빈 칸: 참가자가 이동 가능한 칸
# 벽
# 참가자가 이동할 수 없는 칸
# 1 이상 9 이하 내구도를 가짐
# 회전할 때 내구도가 1 씩 깎임
# 내구도가 0이되면 빈 칸으로 변경

# 출구
# 참가자가 해당 칸에 도달하면 즉시 탈출

# 1초마다 모든 참가자는 한 칸 씩 움직임
# 모든 참가자는 동시에 움직임
# 두 위치의 최단 거리는 abs(x1-x2) + abs(y1-y2)로 정의
# 상하좌우로 이동 가능, 벽으로는 이동 불가능
# 출구까지의 최단거리가 가까워지는 방향으로 이동
# 움직일 수 있는 칸이 2개 이상이면, 상 하로 움직이는 걸 우선
# 참가자가 움직일 수 없는 상황이면 움직이지 않음
# 한 칸에 2명 이상의 참가자가 있을 수 있음

# 미로의 회전
# 모든 참가자가 이동을 끝낸 후 미로가 회전함
# 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형을 잡습니다.
# 2개 이상이면, 우선순위 r 작은거 -> c 작은거
# 시계방향 90도 회전

# K초 동안 위 과정 반복
# K 초 전에 모든 참가자가 탈출에 성공하면 게임이 끝남

# 게임이 끝났을 때, 모든 참가자들의 이동 거리 합과 출구 좌표를 출력

import sys

input = sys.stdin.readline
moved = 0
exit_cnt = 0

def debug(arr, players):
    for num, ci, cj in players:
        if arr[ci][cj] == num:
            continue
        else:
            print('Expected:', num, arr[ci][cj])
            print('players ci, cj:', ci, cj)

def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


def calc_dist(pos1, pos2):
    pos1_i, pos1_j = pos1
    pos2_i, pos2_j = pos2

    return abs(pos1_j - pos2_j) + abs(pos1_i - pos2_i)


def moves():
    global moved
    global exit_cnt

    removed = []
    for idx, (num, ci, cj) in enumerate(players):
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and arr[ni][nj] <= 0 and (calc_dist([ci, cj], exit) > calc_dist([ni, nj], exit)):
                players[idx] = [num, ni, nj]
                if arr[ni][nj] == -100:
                    arr[ci][cj] = 0 if num else arr[ci][cj]
                    removed.append(idx)
                else:
                    arr[ni][nj] = num
                    arr[ci][cj] = 0 if num else arr[ci][cj]
                moved += 1
                break

    for r in sorted(removed, reverse=True):
        players.pop(r)
        exit_cnt += 1

def get_box():
    for length in range(2, N):
        for si in range(N - length + 1):
            for sj in range(N - length + 1):
                exit_valid = False
                player_valid = False
                for i in range(si, si + length):
                    for j in range(sj, sj + length):
                        if (i, j) == (exit[0], exit[1]):
                            exit_valid = True
                        for idx, ci, cj in players:
                            if (i, j) == (ci, cj):
                                player_valid = True
                        if exit_valid and player_valid:
                            return si, sj, length


def rotate(arr, si, sj, length):
    rot_arr = [x[:] for x in arr]
    p_lst = []
    for i in range(length):
        for j in range(length):
            for idx, (num, ci, cj) in enumerate(players):
                if ci == si + length - j - 1 and cj == sj + i:
                    p_lst.append([num, si+i, sj+j])
            rot_arr[si + i][sj + j] = arr[si + length - j - 1][sj + i] - 1 if arr[si + length - j - 1][sj + i] > 0 else \
            arr[si + length - j - 1][sj + i]

    for num, ci, cj in p_lst:
        for i, (num_, _, _) in enumerate(players):
            if num == num_:
                players[i] = [num, ci, cj]

    for i in range(N):
        for j in range(N):
            if rot_arr[i][j] == -100:
                exit = [i, j]

    return rot_arr, exit


N, M, K = map(int, input().strip().split())  # N: 격자 사이즈, M: 참가자 수, K: 초
arr = [list(map(int, input().strip().split())) for _ in range(N)]  # 0은 빈칸, 1이상 9 이하는 벽의 내구도
players = [list(map(lambda x: int(x) - 1, input().strip().split())) for _ in range(M)]

for idx,(i,j) in enumerate(players):
    players[idx] = [-idx-1, i, j]

exit = list(map(lambda x: int(x) - 1, input().strip().split()))
#
# print_map(arr)
# print('---------')

# 참가자 arr에 등록
for idx, i, j in players:
    arr[i][j] = idx

# 탈출구 arr에 등록
arr[exit[0]][exit[1]] = -100

# print_map(arr)
# print('---------')
for T in range(K):
    # 참가자 이동
    moves()
    # print_map(arr)
    # debug(arr, players)
    # print('---------')

    # 정사각형 시작점 찾기
    if exit_cnt == M:
        break
    si, sj, length = get_box()

    # 미로 회전
    arr, exit = rotate(arr, si, sj, length)
    # print_map(arr)
    # debug(arr, players)
    # print('---------')

print(moved)
print(exit[0]+1, exit[1]+1)



