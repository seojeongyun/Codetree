# 격자: NxN

# 금 채굴
    # 마름모 모양으로 가능
        # 마름모의 일부가 격자를 벗어난 경우, 벗어난 영역은 계산하지 않는다
    # 비용: 마름모 안의 격자 개수
        # K^2 + (K+1)^2
    # 금 한 개의 가격이 M일 때, 손해보지 않으면서 채굴할 수 있는 가장 많은 금의 개수

import sys
from collections import deque
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def make_rhombus(i, j, K):
    arr = [[0] * N for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1
    q = deque([[i, j]])

    ij_lst = [[i,j]]
    # ci, cj를 기준으로 상하좌우
    while q:
        ci, cj = q.popleft()
        if v[ci][cj] == K+1:
            break
        for di, dj in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if in_range(ni, nj) and not v[ni][nj]:
                q.append([ni, nj])
                v[ni][nj] = v[ci][cj] + 1
                ij_lst.append([ni, nj])

    return ij_lst

# [0] 입력
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = 0

# K에 따른 마름모의 좌표를 수식으로 자동화할 수 있다면
# 마름모: (K+1) x (K+1) 의 정사각형과 네 개의 모서리(?) 로 구성
    # i,j를 마름모의 중심이라고 하자.
    # 정사각형: (i-K+1, j-K+1) (좌상단) 부터 (i+K-1, j+K-1) (우하단) 까지
    # 모서리:  (i-K, j) / (i, j-K) / (i+K, j) / (i, j+K)

for K in range(N+1): # K의 범위를 N으로 넉넉히 설정
    loss = K**2 + (K+1)**2
    # 마름모 중심점 i,j
    for i in range(N):
        for j in range(N):
            num_gold = 0

            if K == 0:
                num_gold = arr[i][j]
                if num_gold * M >= loss:
                    answer = max(answer, num_gold)
            

            if K > 0:
                # 모서리 좌표 계산 및, 각 좌표가 arr 범위 내에 있을 경우 금 탐색
                ij_lst = make_rhombus(i, j, K)
                for y, x in ij_lst:
                    num_gold += arr[y][x]
                
                # 손해를 보지 않았다면 answer에 금 개수 저장
                if num_gold * M >= loss:
                    answer = max(answer, num_gold)
                    # print(answer, K, i, j)

print(answer)
