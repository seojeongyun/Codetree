# 격자: N x N
    # 각 칸에 거울 존재
        # 거울: \ or / 의 형태

# 격자 밖 4N개의 위치 중 특정 위치에서 레이저를 쏘았을 때 거울에 튕기는 횟수

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

N = int(input().strip())
arr = [[0] * N for _ in range(N)]
v_debug = [[0] * N for _ in range(N)]

# 입력: '/'는 1, '\'는 -1
for i in range(N):
    pattern = input().rstrip()
    for j, p in enumerate(pattern):
        if p == '/':
            arr[i][j] = 1
        else:
            arr[i][j] = -1


# 좌표 및 방향 설정
    # 0 ~ N-1 : 아래 / N ~ 2N-1: 왼쪽 / 2N ~ 3N-1: 위 / 3N ~ 4N-1: 오른쪽
dir = int(input().strip()) 
pos = dir-1
if 0 <= pos < N:
    ci,cj,dir_num = 0, pos, 1
elif N <= pos < 2*N:
    ci,cj,dir_num = pos-N, N-1, 2
elif 2*N <= pos < 3*N:
    ci,cj,dir_num = N-1, (3*N-1)-pos, 3
elif 2*N <= pos < 4*N:
    ci,cj,dir_num = (4*N-1)-pos, 0, 0

# DEBUG
v_debug[ci][cj] = 1

# didj
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)


# 반사
count = 1
while True:
    # 종료 조건: 밖으로 나가면 == 반사가 끝나면
    if not in_range(ci, cj):
        break
    
    # 현재 dir_num 과 /(1) \(-1) 모양에 따라 dir 변경
    # dir_num == 0 and arr[ci][cj] == 1이면, 반시계 90도
    #                  arr[ci][cj] == 0이면, 시계 90도

    # dir_num == 1 and arr[ci][cj] == 1이면, 시계 90도
    #                  arr[ci][cj] == 0이면, 반시계 90도

    # dir_num == 2 and arr[ci][cj] == 1이면, 반시계 90도
    #                  arr[ci][cj] == 0이면, 시계 90도

    # dir_num == 3 and arr[ci][cj] == 1이면, 시계 90도
    #                  arr[ci][cj] == 0이면, 반시계 90도

    if (dir_num == 0 or dir_num == 2) and arr[ci][cj] == 1: # 반시계
        dir_num = (dir_num-1+4) % 4
    elif (dir_num == 0 or dir_num == 2) and arr[ci][cj] == -1: # 시계
        dir_num = (dir_num+1) % 4
    elif (dir_num == 1 or dir_num == 3) and arr[ci][cj] == 1: # 시계
        dir_num = (dir_num+1) % 4
    elif (dir_num == 1 or dir_num == 3) and arr[ci][cj] == -1: # 반시계
        dir_num = (dir_num-1+4) % 4

    
    # ci, cj = ci+di[dir_num], cj+dj[dir_num]
    ni, nj = ci+di[dir_num], cj+dj[dir_num]
    if in_range(ni, nj):
        v_debug[ni][nj] = v_debug[ci][cj] + 1
        count += 1
    ci, cj = ni, nj

print(count)
# for row in v_debug:
#     print(*row)