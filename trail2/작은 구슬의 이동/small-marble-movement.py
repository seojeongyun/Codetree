# 격자: N x N
    # 한 개의 구슬이 놓여있고, 1초에 한 칸 씩 상하좌우중 특정 방향으로 이동

# 구슬의 이동
    # 벽에 부딪히면 움직이는 방향 반대로 이동
    # 방향 바꾸는데 1초 소요
        # 이 순간엔 원래 있던 칸에 그대로 머무름
        # 즉, 벽에 부딪히면 방향만 변경

# 구슬의 처음 위치와 초기 방향이 주어졌을 때, T초가 지난 후의 구슬 위치를 구하시오

import sys
input = sys.stdin.readline

N, T = map(int, input().strip().split())
ci, cj, dir = input().strip().split() # ci, cj 는 str
ci, cj = int(ci), int(cj)

dir_dict = {
    'U': 2,
    'D': 1,
    'R': 0,
    'L': 3
}

di, dj = (0, 1, -1, 0), (1, 0, 0, -1) # dir_num 0과 3을 쌍으로, 1과 2를 쌍으로.
dir_num = dir_dict[dir]

for _ in range(T):
    ni, nj = ci + di[dir_num], cj + dj[dir_num]
    
    if dir_num == 0 or dir_num == 3: # 좌우 이동
        if nj == N+1 or nj == 0: # 벽에 부딪히면 방향만 바꿈
            dir_num = 3 - dir_num
        else: # 벽에 부딪히지 않으면 앞으로 전진
            ci, cj = ni, nj

    if dir_num == 1 or dir_num == 2:
        if ni == N+1 or ni == 0:
            dir_num = 3 - dir_num
        else:
            ci, cj = ni, nj

    # print(ci, cj)
print(ci, cj)

