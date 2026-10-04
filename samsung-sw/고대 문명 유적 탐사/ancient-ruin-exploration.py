# 격자: 5 x 5
    # 각 칸에는 1부터 7까지 유물 조각 배치

# 탐사 진행
    # 3 x 3 격자 선택 후 90, 180, 270 도 중 하나만큼 회전
    # 회전 목표
        # 유물 1차 획득 가치를 최대화
        # 그런 방법이 여러개인 경우 회전한 각도가 가장 작은 방법 선택

# 유물 획득
    # 유물 1차 획득
        # 상하좌우로 인접한 같은 종류의 유물 조각은 연결되어 있음
        # 이 조각이 3개 이상 연결된경우 조각이 모여 유물이 되고 사라짐
    # 유물의 가치
        # 모인 조각의 개수

# 유물 생성
    # 조각이 사라진 위치에는 유적의 벽면에 적혀있는 순서대로 새로운 조각이 생김
    # 열 번호가 작은 순으로 조각이 생기고, 열 번호가 같다면 행 번호가 큰 순

    # 유적의 벽면
        # 1부터 7 사이의 숫자가 M개
        # 유적에서 조각이 사라졌을 때 새로 생겨나는 조각에 대한 정보를 담고 있음
        # 벽면에 있는 숫자르 사용한 이후에는 다시 사용할 수 없다.

# 유물 연쇄 획득
    # 새로운 유물이 생겨난 이후에도 3개 이상 연결될 수 있다.
    # 이 경우 앞과 같은 방식으로 조각이 유물이 되어 사라짐
    # 사라진 위치에는 또 다시 새로운 조각이 생겨나며 이는 더이상 조각이 3개 이상 연결되지 않을 때 까지 반복

# 탐사 반복
    # 탐사 진행 ~ 유물 연쇄 획득까지 1턴으로 생각
    # K턴 진행
    # 탐사 진행 과정에서 어떤 방법으로도 유물을 획득할 수 없다면 그 즉시 종료

# 출력
    # 각 턴마다 획득한 유물의 가치 총합을 출력

import sys
from collections import deque

input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(*row)

def in_range(i, j):
    return 0 <= i < 5 and 0 <= j < 5

def rotate(ci, cj, arr):
    rot_arr = [row[:] for row in arr]

    a, b, c = arr[ci - 1][cj - 1:cj + 2]
    for i, v in ((ci - 1, a), (ci, b), (ci + 1, c)):
        rot_arr[i][cj + 1] = v

    lst = []
    for i in (ci - 1, ci, ci + 1):
        lst.append(arr[i][cj + 1])
    rot_arr[ci + 1][cj - 1:cj + 2] = lst[::-1]

    a, b, c = arr[ci + 1][cj - 1:cj + 2]
    for i, v in ((ci - 1, a), (ci, b), (ci + 1, c)):
        rot_arr[i][cj - 1] = v

    lst = []
    for i in (ci - 1, ci, ci + 1):
        lst.append(arr[i][cj - 1])
    rot_arr[ci - 1][cj - 1:cj + 2] = lst[::-1]

    return rot_arr

def bfs(i, j, v, arr, target):
    q = deque([(i, j)])
    cnt = 1
    lst = [[i, j]]
    while q:
        ci, cj  = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and arr[ni][nj] == target:
                q.append([ni, nj])
                v[ni][nj] = 1
                cnt += 1
                lst.append([ni, nj])

    if cnt >= 3:
        return v, cnt, lst

    else:
        return v, 0, []

def get_score(arr, remove):
    score = 0
    v = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if not v[i][j]:
                v[i][j] = 1
                v, cnt, lst = bfs(i, j, v, arr, arr[i][j])

                if remove:
                    if len(lst) > 2:
                        for ri, rj in lst:
                            arr[ri][rj] = 0
                score += cnt
    return score

# [입력]
K, M = map(int, input().strip().split())  # K는 턴 수, M은 벽에 적힌 유물 조각의 개수
arr = [list(map(int, input().strip().split())) for _ in range(5)]
walls = list(map(int, input().strip().split()))

walls_idx = 0
for k in range(K):
    value = 0
    # [회전 결정]
    rotate_info = [-1, [4, 0, 0]]
    for i in range(1, 4):
        for j in range(1, 4):
            ci, cj = i, j  # 회전 중심점

            # 회전 시뮬레이션
            for degree in range(3):
                if degree == 0:
                    rotated_arr = rotate(ci, cj, arr)
                else:
                    rotated_arr = rotate(ci, cj, rotated_arr)

                # print_map(rotated_arr)
                # print('-------')

                # 유물의 1차 가치 판단
                score = get_score(rotated_arr, remove=False)
                if rotate_info[0] < score:
                    rotate_info[0] = score
                    rotate_info[1] = [degree, ci, cj]

                elif rotate_info[0] == score:
                    if rotate_info[1][0] > degree:
                        rotate_info[0] = score
                        rotate_info[1] = [degree, ci, cj]

                    elif rotate_info[1][0] == degree:
                        if rotate_info[1][2] > cj:
                            rotate_info[0] = score
                            rotate_info[1] = [degree, ci, cj]

                        elif rotate_info[1][2] == cj:
                            if rotate_info[1][1] > ci:
                                rotate_info[0] = score
                                rotate_info[1] = [degree, ci, cj]

    if rotate_info[0] == 0:
        break

    # [1차 가치가 높은 회전 정보로 회전]
    for degree in range(rotate_info[1][0]+1):
        ci, cj = rotate_info[1][1], rotate_info[1][2]
        if degree == 0:
            rotated_arr = rotate(ci, cj, arr)
        else:
            rotated_arr = rotate(ci, cj, rotated_arr)

    # [유물 연쇄 획득]
    while True:
        score = get_score(rotated_arr, remove=True)
        # print_map(rotated_arr)
        # print('-------')
        value += score

        if score < 3:
            break

        # [유물 생성]
        for j in range(5):
            for i in range(5-1, -1, -1):
                if not rotated_arr[i][j]:
                    rotated_arr[i][j] = walls[walls_idx]
                    walls_idx += 1

        # print_map(rotated_arr)
        # print('-------')

    print(value, end=' ')
    arr = [row[:] for row in rotated_arr]

    # print_map(rotated_arr)