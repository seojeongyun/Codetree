# 격자: N x N

# 구슬
# M 개
# 각 구슬은 1초에 한 칸 씩 이동
# 벽에 충돌하면 방향 전환
# 구슬끼리 충돌하면 구슬 사라짐
# 이동중 만나는 경우는 충돌로 간주 X


import sys

input = sys.stdin.readline


def in_range(i, j):
    return 0 <= i < N and 0 <= j < N


T = int(input().strip())
TIME = 100

# di, dj, dir
di, dj = (-1, 0, 1, 0), (0, 1, 0, -1)
dir_dict = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3
}

for _ in range(T):
    N, M = map(int, input().strip().split())
    info = [list(input().strip().split()) for _ in range(M)]

    # 구슬 좌표 관리 리스트
    coords = []
    for i, j, dir in info:
        dir_num = dir_dict[dir]
        coords.append([dir_num, [int(i) - 1, int(j) - 1]])

    for _ in range(TIME):
        # 이동
        for idx in range(len(coords)):
            # print('start', coords[idx])
            dir_num, coord = coords[idx]
            ci, cj = coord
            #
            ni, nj = ci + di[dir_num], cj + dj[dir_num]

            # 충돌 시 방향만
            if not in_range(ni, nj):
                dir_num = (dir_num + 2) % 4
                coords[idx] = [dir_num, [ci, cj]]

            else:
                coords[idx] = [dir_num, [ni, nj]]
            # print('end', coords[idx])

        # 충돌 여부 판단을 위해 2차원 격자에 구슬 등록
        arr = [[0] * N for _ in range(N)]
        for _, c in coords:
            i, j = c
            arr[i][j] += 1

        # for row in arr:
        #     print(*row)
        # print('--------')

        removed_idx = []
        for idx, (_, c) in enumerate(coords):
            i, j = c
            if arr[i][j] > 1:
                removed_idx.append(idx)

        # 충돌한 구슬 제거
        for idx in sorted(removed_idx, reverse=True):
            coords.pop(idx)

    print(len(coords))


