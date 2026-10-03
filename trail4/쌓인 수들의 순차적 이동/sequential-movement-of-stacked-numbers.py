# 격자: N x N
# 1 이상 N x N 이하의 정수들이 한 번 씩만 등장

# 이동
# M번
# 각 위치에서 8방향에 대해 가장 큰 값이 있는 곳으로 이동
# 인접 칸에 여러 값이 쌓여있다면 스택의 어느 위치에 있든 관계없이 모든 정수를 대상으로 가장 큰 값을 찾음

# 이동할 정수 위에 다른 정수들이 쌓여있는 경우, 위에 쌓여있는 정수들도 순서를 유지한 채 함께 이동
# 이동할 정수 아래 깔려있던 정수들은 그자리에 그대로 남음
# 이동한 위치에 이미 다른 정수가 있는 경우에는 옮겨진 정수들이 그 위에 순서대로 쌓임

# M번 움직인 이후의 상태를 출력

import sys

input = sys.stdin.readline


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def find_idx(num):
    for i in range(N):
        for j in range(N):
            for k in range(len(arr[i][j])):
                if arr[i][j][k] == num:
                    return [i, j, k]

N, M = map(int, input().strip().split())
data = [list(map(int, input().strip().split())) for _ in range(N)]
nums = list(map(int, input().strip().split()))

arr = [[0] * N for _ in range(N)]

# 배열 3차원으로 변환
for i in range(N):
    for j in range(N):
        arr[i][j] = [data[i][j]]

# M번 반복
for num in nums:
    # num 위치 찾기
    ci, cj, ck = find_idx(num)
    mi, mj = ci, cj
    max_val = 0

    # 8방향 탐색
    for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1)):
        ni, nj = ci + di, cj + dj
        if in_range(ni, nj):
            for k in range(len(arr[ni][nj])):
                if max_val < arr[ni][nj][k]:
                    max_val = arr[ni][nj][k]
                    mi, mj = ni, nj

    if (mi, mj) != (ci, cj):
        for v in arr[ci][cj][ck:]:
            arr[mi][mj].append(v)
        arr[ci][cj] = arr[ci][cj][:ck]

    # for row in arr:
    #     print(*row)

for row in arr:
    for col in row:
        if col == []:
            print('None')
        else:
            print(*col[::-1])