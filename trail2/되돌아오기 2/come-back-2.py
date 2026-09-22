# (0, 0) 시작

# 명령어
    # L: 왼쪽으로 90도 전환
    # R: 오른쪽으로 90도 전환
    # F: 바라보는 방향으로 한 칸 이동
    # 각 명령어 수행은 1초가 걸림

# 명령을 수행하다가 다시 (0,0)으로 되돌아오는게 몇 초 뒤인지 구하고, 돌아오지 못하면 -1 출력

import sys
input = sys.stdin.readline

# 입력
commands = input().strip()

# didj, dir
ci, cj, dir_num = 0, 0, 3
di, dj = (0, 1, 0, -1), (1, 0, -1, 0)

time = 0
for cmd in commands:
    if cmd == 'L':
        dir_num = (dir_num -1 + 4) % 4

    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4

    else:
        ci, cj = ci+di[dir_num], cj+dj[dir_num]
    
    time += 1

    if (ci, cj) == (0, 0):
        break

else:
    time = -1
    
print(time)
