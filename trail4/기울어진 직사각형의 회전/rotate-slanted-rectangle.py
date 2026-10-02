# 격자: N x N
    # 1이상 100 이하

# 기울어진 직사각형을 잡아 회전

import sys
from collections import deque
input = sys.stdin.readline

def get_rect(ci, cj, dir, m):
    # ni, nj = ci + di[dir], cj + dj[dir]
    # arr[ni][nj] = tmp_lst.popleft()
    # ci, cj = ni, nj

    for i in range(m):
        ni, nj = ci + di[dir], cj + dj[dir]
        tmp_lst.append(arr[ni][nj])
        arr[ni][nj] = tmp_lst.popleft()
        
        ci, cj = ni, nj
    # print(tmp_lst)
    return ni, nj

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
info = list(map(int, input().strip().split())) 

# 기울어진 직사각형에 해당하는 좌표값을 담는 리스트
coords_lst = []

# 시작 지점: ci, cj
# 각 방향으로 이동하는 거리: m1, m2, m3, m4
# 회전 방향: dir(0이면 반시계, 1이면 시계)
ci, cj, m1, m2, m3, m4, dir = info
ci, cj = ci - 1, cj - 1

# 1, 2, 3, 4 방향 순으로 di, dj 설정
if dir == 0:
    di, dj = (-1, -1, 1, 1), (1, -1, -1, 1)
else:
    di, dj = (-1, -1, 1, 1), (-1, 1, 1, -1)
#
tmp_lst = deque([arr[ci][cj]])

# 1번 방향부터 4번 방향까지
if dir == 0:
    rotate = (0, m1), (1, m2), (2, m3), (3, m4)
else:
    rotate = (0, m4), (1, m3), (2, m2), (3, m1)

for dir_num, m in rotate:
    # m값 만큼 이동
    ci, cj = get_rect(ci, cj, dir_num, m)

# debug
# print(coords_lst)

for row in arr:
    print(*row)

    