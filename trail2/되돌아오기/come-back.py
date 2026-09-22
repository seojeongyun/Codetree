# (0,0) 출발
# 이동
    # N번에 걸쳐 움직이려는 방향과 거리가 주어짐
        # N 3
        # E 2 ..
    # 1초에 한 칸 이동

# 몇 초 뒤 다시 (0, 0)으로 돌아오는지 계산, 돌아오지 못하면 -1 출력

import sys
input = sys.stdin.readline
answer = 0

def moves(cmd):
    global ci, cj
    
    time = 0
    for dir, dist in cmd:
        di, dj = directions[dir]

        for t in range(1, int(dist)+1):
            ci, cj = ci+di, cj+dj
            time += 1

            if (ci, cj) == (0, 0):
                return time

    return -1

# 입력
N = int(input().strip())
cmd = [input().strip().split() for _ in range(N)]

# didj, dir
ci, cj= 0, 0
directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, -1),
    'W': (0, 1)
}

# 이동
time = moves(cmd)
print(time)