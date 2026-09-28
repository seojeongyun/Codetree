# 격자: N x M
# 바람
    # Q번 붊
    # 특정 행의 모든 원소를 왼쪽 혹은 오른쪽으로 한 칸 shift

# 전파
    # 1 Cycle
        # 바람에 의해 한 칸 shift된 이후 위 아래 행을 순차적으로 체크
        # 현재 행이 shift된 이후, 단 하나라도 같은 열에 같은 숫자가 적혀있으면 전파 진행 (위, 아래 각각 진행)
        # 같은 숫자가 하나도 존재하지 않거나 끝(row기준)에 다다르면 전파를 종료
        # 전파가 진행되는 경우 바람의 방향과 반댓방향으로 한 칸 씩 shift
        # 예를 들어 5x5 행렬에서, 바람이 3행에 불었으면 2행과 3행의 각 열 비교, 3행과 4열의 각 열 비교 후 일치하는 경우 바람 반댓 방향으로 shift

    # 2 Cycle
        # 1행과 2행 비교, 4행과 5행 비교하여 동일하게 전파 진행

# N x N 격자 아니므로 위가 아래보다 먼저 끝날 수도 있고, 아래가 위보다 먼저 끝날 수 있음. in_range 함수를 사용해서 valid 유무 판단 후 전파 진행

import sys
input = sys.stdin.readline

def rotate(arr, row, dir_num):
    lst = arr[row]
    if dir_num == 0: # >> 1
        lst = [lst[-1]] + lst[:-1]
        arr[row] = lst
    else: # << 1
        lst = lst[1:] + [lst[0]]
        arr[row] = lst
    
    return arr

def compared_column(arr, row):
    global M
    for j in range(M):
        if arr[row-1][j] == arr[row][j]:
            return True

    return False

def spread(arr, row, dir_num):
    u_dir_num, u_row = dir_num, row
    d_dir_num, d_row = dir_num, row
    # 조건 부합 안하면 전파 안하니까 그냥 N번 반복하면 알아서 전파 끝나있을듯
    for _ in range(N):
        # 위 전파: row-1 > -1 인 경우만
        if u_row-1 > -1:
            # 행 비교
            if compared_column(arr, u_row):
                # 전파 진행
                u_dir_num = (u_dir_num+1) % 2
                arr = rotate(arr, u_row-1, u_dir_num)
                u_row = u_row - 1
    
    for _ in range(N):
        # 아래 전파: row+1 < N인 경우만
        if d_row+1 < N:
            if compared_column(arr, d_row+1):
                d_dir_num = (d_dir_num+1) % 2
                arr = rotate(arr, d_row+1, d_dir_num)
                d_row = d_row+1
    
    return arr

# 입력
N, M, Q = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
wind = [input().strip().split() for _ in range(Q)]

# dir
dir_lst = ['L', 'R']

for row, dir in wind:
    row = int(row)-1
    dir_num = dir_lst.index(dir)

    # 바람에 의한 이동
    arr = rotate(arr, row, dir_num)

    # 전파
    arr = spread(arr, row, dir_num)

for row in arr:
    print(*row)

    