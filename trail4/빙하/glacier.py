# 격자: N x M
    # 1은 빙하를, 0은 물을 의미
    # 격자 바깥은 항상 빙하가 아니고, 빙하를 제외한 나머지는 물

# 바깥물
    # 격자의 가장자리에 있는 물 칸끼리 이동해서 도달할 수 있으면
    # 인접한 빙하 칸을 녹임

# 빙하로 둘러싸인 물
    # 사방이 빙하로 막혀 도달할 수 없는 물
    # 빙하를 녹일 수 없음

# 녹는 현상
    # 매 초 시작 지점의 격자 상태를 기준으로, 바깥물에 의해 상하좌우로 인접한 빙하 칸을 동시에 녹임
    # 이번 초에 녹은 빙하 칸들은 다음 초부터 물로 취급
        # 같은 초 안에서는 연쇄적으로 녹지 않음

# 빙하가 전부 녹는데 걸리는 시간과, 마지막 초에 녹아 사라지는 빙하 칸의 개수를 구해라.

import sys
from collections import deque
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs(start):
    si, sj = start
    v[si][sj] = 1
    #
    q = deque([start])
    #
    lst = [[si, sj]]
    while q:
        ci, cj = q.popleft()
        #
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and not v[ni][nj] and not arr[ni][nj]:
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    lst.append([ni, nj])

    return lst

def ice_break(coords):
    cnt = 0
    for ci, cj in coords:
        for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ni, nj = ci + di, cj + dj
            if in_range(ni, nj) and arr[ni][nj]:
                arr[ni][nj] = 0
                cnt += 1
    
    return cnt

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
TIME = 100
#

for t in range(TIME):
    sum_val = 0
    v = [[0] * M for _ in range(N)]
    start = (0, 0)
    
    # 바깥물 좌표 획득
    coords = bfs(start)
    # print(coords)

    # 인접한 얼음 녹이기
    cnt = ice_break(coords)
    # for row in arr:
    #     print(*row)
    # print('--------')
    # print(cnt)

    # 종료 조건 체크
    for i in range(N):
        for j in range(M):
            sum_val += arr[i][j]

    if sum_val == 0:
        break

print(t+1, cnt)
            

# 얼음 녹일 방법
# v를 초기화해야하냐 말아야하냐