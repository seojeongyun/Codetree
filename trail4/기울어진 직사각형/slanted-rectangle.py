# 격자: N x N
# 기울어진 직사각형
# 격자 내 한 지점으로부터 대각선으로 움직이며 반시계 방향 순회
# 1,2,3,4번 방향순으로 순회해야하며 각 방향으로 최소 1번 움직여야함
# 이동 중 격자 밖으로 넘어가선 안됨

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


import sys

input = sys.stdin.readline
answer = 0
# 입력
N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# di, dj, dir_num
# IDEA: dir_num으로 순회 방향 지정
di, dj = (-1, -1, 1, 1), (1, -1, -1, 1)

# 첫 2중 for-loop은 ci, cj 를 순회하는 것이 목적
lst = []
for row in range(N):
    for col in range(N):
        ci, cj = row, col
        ur_lst = []  # 우상단으로 순회하는 좌표를 담을 list
        # 4중 for-loop
        # 각 loop은 dir_num = 0, 1, 2, 3 순서로 순회
        # 이동 중 격자 밖으로 넘어가면 해당 loop을 탈출
        # 마주보는 방향의 lst 원소 개수가 동일한 경우 == 기울어진 직사각형으로 순회했다고 할 수 있을듯
        for i in range(1, N+1):  # i는 dir_num = 0 방향으로 최대 이동 횟수를 의미
            ul_lst = []  # 좌상단으로 순회하는 좌표를 담을 list
            dir_num = 0
            #
            ni, nj = ci + di[dir_num], cj + dj[dir_num]
            if not in_range(ni, nj):
                break

            ur_lst.append((ni, nj))
            #
            for j in range(1, N+1):  # j는 dir_num = 1 방향으로 최대 이동 횟수를 의미
                ci, cj = ni, nj
                #
                lb_lst = []  # 좌하단으로 순회하는 좌표를 담을 list
                dir_num = 1
                #
                ni, nj = ci + di[dir_num], cj + dj[dir_num]
                if not in_range(ni, nj):
                    ci, cj = ni - (j * di[dir_num]), nj - (j * dj[dir_num])
                    break

                ul_lst.append((ni, nj))
                #
                for k in range(1, N+1):  # k는 dir_num = 2 방향으로 최대 이동 횟수를 의미
                    ci, cj = ni, nj
                    #
                    rb_lst = []  # 우하단으로 순회하는 좌표를 담을 list
                    dir_num = 2
                    #
                    ni, nj = ci + di[dir_num], cj + dj[dir_num]
                    if not in_range(ni, nj):
                        ni, nj = ni - (k * di[dir_num]), nj - (k * dj[dir_num])
                        break

                    lb_lst.append((ni, nj))
                    #
                    for l in range(1, N+1):  # l은 dir_num = 3 방향으로 최대 이동 횟수를 의미
                        ci, cj = ni, nj
                        #
                        dir_num = 3
                        #
                        ni, nj = ci + di[dir_num], cj + dj[dir_num]
                        if not in_range(ni, nj):
                            ni, nj = ni - (l * di[dir_num]), nj - (l * dj[dir_num])
                            break

                        rb_lst.append((ni, nj))

                        if len(ur_lst) == len(lb_lst) and len(ul_lst) == len(rb_lst):
                            # mutable
                            lst.append([ur_lst[::], lb_lst[::], ul_lst[::], rb_lst[::]])

# 정답 처리
for coords_lst in lst:
    sum_val = 0
    for coords in coords_lst:
        for i, j in coords:
            sum_val += arr[i][j]
    answer = max(answer, sum_val)

print(answer)