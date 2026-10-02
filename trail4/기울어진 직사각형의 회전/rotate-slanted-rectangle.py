# 격자: N x N
    # 1이상 100 이하

# 기울어진 직사각형을 잡아 회전

import sys
input = sys.stdin.readline

def get_rect(ci, cj, dir, m):
    for i in range(m):
        ni, nj = ci + di[dir], cj + dj[dir]
        ci, cj = ni, nj
        coords_lst.append((ni,nj))
    return ni, nj

def rotate(dir):
    if dir == 0:
        tmp = arr[coords_lst[-1][0]][coords_lst[-1][1]]
        rotate_range = range(len(coords_lst)-1, 0, -1)
        for idx in rotate_range:
            i1, j1 = coords_lst[idx]
            i2, j2 = coords_lst[idx-1]
            arr[i1][j1] = arr[i2][j2]
        arr[coords_lst[0][0]][coords_lst[0][1]] = tmp

    else:
        tmp = arr[coords_lst[0][0]][coords_lst[0][1]]
        rotate_range = range(0, len(coords_lst)-1)
        for idx in rotate_range:
            i1, j1 = coords_lst[idx]
            i2, j2 = coords_lst[idx+1]
            arr[i1][j1] = arr[i2][j2]
        arr[coords_lst[-1][0]][coords_lst[-1][1]] = tmp

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
di, dj = (-1, -1, 1, 1), (1, -1, -1, 1)

# 1번 방향부터 4번 방향까지
for dir_num, m in ((0, m1), (1, m2), (2, m3), (3, m4)):
    # m값 만큼 이동
    ci, cj = get_rect(ci, cj, dir_num, m)

# debug
# print(coords_lst)

# coords_lst에 있는 좌표값 순서대로 >> 1
rotate(dir)

for row in arr:
    print(*row)

    