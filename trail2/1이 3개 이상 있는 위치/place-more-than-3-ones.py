# 격자: N x N
    # 0과1 로 구성
# 각 칸에 대해 상하좌우로 인접한 칸 중 1이 적힌 칸 수가 3개 이상인 칸의 개수 세기
# 격자를 벗어나는 경우는 1이 적혀있지 않은 것으로 간주

import sys
input = sys.stdin.readline
answer = 0

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        cnt = 0
        ci, cj = i, j
        for di, dj in ((-1, 0),(1, 0),(0, 1),(0, -1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and arr[ni][nj] == 1:
                cnt += 1

        if cnt >= 3:
            answer += 1

print(answer)