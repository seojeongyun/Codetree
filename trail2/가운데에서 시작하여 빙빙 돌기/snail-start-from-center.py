# 격자: N x N
    # 가운데서 시작해서 시계방향 달팽이
        # dir_num 갱신 조건이 더 복잡해짐

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

# 입력    
N = int(input().strip())

# 격자
arr = [[0] * N for _ in range(N)]

# didj, dir_num
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
dir_num = 0

# 초기화
ci, cj = N//2, N//2
arr[ci][cj] = 1
dist = 1

for i in range(2, N*N+1):
    ni, nj = ci + di[dir_num], cj + dj[dir_num]

    # dir_num 회전 조건
    # ni == ci 면서 cj == N//2 + 1
    # nj == cj 면서 ci == N//2 - 1
    # ni == ci 면서 cj == N//2 - 1
    # nj == cj 면서 ci == N//2 + 1
    # 여기까지가 한 바퀴
    # 다음 바퀴부터는 2로 증가
    # ni == ci 면서 cj == N//2 + 2
    # nj == cj 면서 ci == N//2 - 2
    # ni == ci 면서 cj == N//2 - 2
    # nj == cj 면서 ci == N//2 + 2
    # changed_dir_cnt를 사용해서 N//2 +- X 의 X만 조절

    if ni == ci and cj == (N//2 + dist):
        dir_num = (dir_num - 1 + 4) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]

    elif nj == cj and ci == (N//2 - dist):
        dir_num = (dir_num - 1 + 4) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]
    
    elif ni == ci and cj == (N//2 - dist):
        dir_num = (dir_num - 1 + 4) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]
    
    elif nj == cj and ci == (N//2 + dist):
        dir_num = (dir_num - 1 + 4) % 4
        ni, nj = ci + di[dir_num], cj + dj[dir_num]
        dist += 1

    arr[ni][nj] = i
    ci, cj = ni, nj

    # Debug
    # for row in arr:
    #     print(*row)
    # print('--------------')

for row in arr:
    print(*row)