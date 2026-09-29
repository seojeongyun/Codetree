# 격자: N x M
# Q번의 바람
    # 특정 영역의 경계에 있는 정수를 시계방향으로 한 칸 씩 shift
    # 해당 직사각형 영역에 있는 값들을 각각 자신의 위치를 기준으로 인접한 원소들과의 평균값으로 바꿈
        # 소수점은 버림
        # 순차적X 동시발생 O


'''
예시 

[1]                 [2]                 [3]
4 5 2 5 0 6    |    4 5 2 5 0 6    |    4 5 2 5 0 6
2 6 1 0 5 5    |    2 1 6 1 0 6    |    2 3 2 2 3 4
5 1 2 1 6 6    |    5 2 2 1 6 5    |    5 3 2 3 4 5
4 2 5 2 8 8    |    4 5 2 8 8 6    |    4 3 4 4 7 6

[1] -> [2] (3행의 2 1 6을 기준으로 시계방향 회전)
[2] -> [3] 직사각형 영역 내의 값들이 상하좌우+현재칸 값 의 평균으로 변함.

'''

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def get_avg_arr(arr, ul, br):
    ul_r, ul_c = ul
    br_r, br_c = br
    #
    new_arr = [row[:] for row in arr]

    for i in range(ul_r, br_r+1):
        for j in range(ul_c, br_c+1):
            val = arr[i][j]
            cnt = 1
            #
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if in_range(ni, nj):
                    val += arr[ni][nj]
                    cnt += 1
            new_arr[i][j] = int(val / cnt)
            
    return new_arr

def rotate(arr, ul, br):
    ul_r, ul_c = ul
    br_r, br_c = br
    tmp1, tmp2 = 0, 0
    
    # 회전 구현: 
    # [1] tmp1에 ul_r, br_c 값 저장
    tmp1 = arr[ul_r][br_c]

    # [2] ul_r, ul_c부터 ul_r, br_c까지 >> 1
    
    arr[ul_r][ul_c:br_c+1] = [0]+arr[ul_r][ul_c:br_c]

    # [4] tmp2에 br_r, br_c 값 저장
    tmp2 = arr[br_r][br_c]
    
    # [5] ul_r, br_c부터 br_r, br_c 까지 한 칸 이동
    for i in range(br_r, ul_r, -1):
        arr[i][br_c] = arr[i-1][br_c]

    # [6] ul_r+1, br_c에 tmp1 대입
    arr[ul_r+1][br_c] = tmp1

    # [7] tmp1에 br_r, ul_c 값 저장
    tmp1 = arr[br_r][ul_c]

    # [8] br_r, br_c부터 br_r, ul_c 까지 << 1 + br_r,br_c에 tmp2 대입
    arr[br_r][ul_c:br_c] = arr[br_r][ul_c+1:br_c]+[tmp2]

    # [9] br_r, ul_c부터 ul_r, ul_c 까지 한 칸 이동
    for i in range(ul_r, br_r):
        arr[i][ul_c] = arr[i+1][ul_c]

    # [10] ul_r, ul_c에 tmp1 대입
    arr[br_r-1][ul_c] = tmp1

    return arr


# 입력
N, M, Q = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
# for row in arr:
#     print(row)
# print('-------')
commands = [list(map(int, input().strip().split())) for _ in range(Q)]

for r1, c1, r2, c2 in commands:
    # 좌표 전처리
    ul = (r1-1, c1-1)
    br = (r2-1, c2-1)

    # 회전
    arr = rotate(arr, ul, br)

    # Debug
    # for row in arr:
    #     print(row)

    # 값 대치: 동시 변환
    # arr에 갱신 X 새로운 곳에 저장
    arr = get_avg_arr(arr, ul, br)

for row in arr:
    print(*row)
