# (0,0)에서 시작, N번 이동
    # 방향과 움직일 거리가 주어짐

# 최종 위치 출력

import sys
input = sys.stdin.readline

N = int(input().strip())
cmd = [input().strip().split() for _ in range(N)]

didj = {
    'N': (1, 0),
    'W': (0, -1),
    'S': (-1, 0),
    'E': (0, 1)
}

ci, cj = 0, 0
for dir, dist in cmd:
    di, dj = didj[dir]
    ci, cj = ci + di*int(dist), cj + dj*int(dist)

print(cj, ci)