# 격자: N x N
    # 시작: 가운데 위치에서 북쪽을 향한 채

# 명령
    # T개
    # L: 왼쪽으로 90도 방향 전환
    # R: 오른쪽으로 90도 방향 전환
    # F: 바라보는 방향으로 한 칸 이동

# 위치를 이동할 때 마다 해당 칸에 적힌 수를 계속 더할 때 최종합을 구하는 프로그램

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

# 입력
N, T = map(int, input().strip().split())
commands = input().strip()
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# didj, dir
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)
dir_num = 3

# 초기화
ci, cj = N//2, N//2
answer = arr[ci][cj] # 시작 위치를 포함해서 누적하기 때문에

for cmd in commands:
    if cmd == 'L': # 왼쪽 90도
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == 'R': # 오른쪽 90도
        dir_num = (dir_num + 1) % 4
    else: # 전진
        ni, nj = ci + di[dir_num], cj + dj[dir_num]
        if in_range(ni, nj):
            answer += arr[ni][nj]
            ci, cj = ni, nj

print(answer)
