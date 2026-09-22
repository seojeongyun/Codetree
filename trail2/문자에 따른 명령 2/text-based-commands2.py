# (0,0) 에서 북쪽을 향한 상태로 시작
# 명령 문자열 S가 주어지면 순서대로 명령어 수행
    # L: 왼쪽으로 90도 회전
    # R: 오른쪽으로 90도 회전
    # F: 현재 바라보는 방향으로 한 칸 이동

# 최종 위치 출력

import sys
input = sys.stdin.readline

command = input().strip()
ci, cj, dir_num = 0, 0, 3
di, dj = (0, -1, 0, 1), (1, 0, -1, 0)

for cmd in command:
    if cmd == 'L': # 반시계 90도
        dir_num = (dir_num - 1 + 4) % 4
    
    elif cmd == 'R': # 시계 90도
        dir_num = (dir_num + 1) % 4
    
    else:
        ci, cj = ci + di[dir_num], cj + dj[dir_num]

print(cj, ci)
    