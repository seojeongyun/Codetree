# 격자 : N x N

# 폭발
    # 특정 열을 선택하면 해당 열에 정수가 적혀있는 위치 중 가장 위에 있는 칸을 중심으로 십자 모양 폭탄 터짐
    # 십자 모양 칸 수는 선택된 칸에 있는 정수로 정해짐
    # 이후 중력에 의해 정수들이 아래로 떨어짐

import sys
input = sys.stdin.readline

def print_map(string, arr):
    print(string)
    for row in arr:
        print(*row)

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def boom(j):
    # 가장 작은 i값 찾기
    for i in range(N):
        if arr[i][j]:
            si, sj = i, j
            value = arr[si][sj]
            arr[si][sj] = 0
            break
    
    else:
        return

    # 폭발
    if value > 1:
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ci, cj = si, sj
            for _ in range(value-1):
                ni, nj = ci + di , cj + dj
                if in_range(ni, nj):
                    arr[ni][nj] = 0
                    ci, cj = ni, nj

def drop():
    new_arr = [[0] * N for _ in range(N)]

    for j in range(N):
        cnt = 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i][j]:
                new_arr[len(arr)-1-cnt][j] = arr[i][j]
                cnt += 1
    
    for i in range(N):
        for j in range(N):
            arr[i][j] = new_arr[i][j]

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
col = [int(input().strip()) for _ in range(M)]

for j in col:
    # 폭발
    boom(j-1)
    # print_map('after boom:', arr)
    
    # 중력
    drop()
    # print_map('after drop:', arr)
    # print('-------------')

for row in arr:
    print(*row)