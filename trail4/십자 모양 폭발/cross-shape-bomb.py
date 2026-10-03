# 격자: N x N

# 폭발
    # 특정 위치를 선택하면, 그 위치를 중심으로 십자 모양으로 폭발
    # 십자모양의 크기는 선택된 위치에 적힌 정수로 정해짐
        # 정수가 1이면 자기 자신만 터지고
        # 2인 경우는 자신을 포함해 상하좌우 방향으로 각각 1개씩
        # 3인 경우는 자신을 포함한 상하좌우 방향으로 각각 2개씩
        # 격자 범위 내에서만 폭발한다.
# 중력
    # 폭발 이후 중력에 의해 정수들이 아래로 떨어짐

import sys
input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def drop():
    global arr

    tmp_arr = [[0] * N for _ in range(N)]
    for j in range(N):
        cnt = 0
        for i in range(N-1, -1, -1):
            if arr[i][j]:
                tmp_arr[N-1-cnt][j] = arr[i][j]
                cnt += 1

    # arr = ... 로 arr 자체를 바꿔버리려고 하면 UnboundLocalError: local variable 'arr' referenced before assignment 발생
        # 이런 경우 global 을 사용
    # arr[:] = ... 는 arr의 원소를 바꾸는 거라서 괜찮음.
    arr = [row[:] for row in tmp_arr]

def boom(i, j):
    ci, cj = i, j
    value = arr[ci][cj]
    if value > 1:
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ci, cj = i, j
            for _ in range(value-1):
                ni, nj = ci + di, cj + dj
                if in_range(ni, nj):
                    arr[ni][nj] = 0
                    ci, cj = ni, nj


    arr[i][j] = 0

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
i, j = map(int, input().strip().split())

#
boom(i-1, j-1)
# print_map(arr)
# print('-----')

#

drop()
print_map(arr)

