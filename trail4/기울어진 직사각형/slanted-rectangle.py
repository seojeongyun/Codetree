n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

answer = 0


def get_rectangle(y, x, len_y, len_x):
    coords = []

    # 우상 → 좌상 → 좌하 → 우하
    directions = [
        (-1, 1, len_y),
        (-1, -1, len_x),
        (1, -1, len_y),
        (1, 1, len_x)
    ]

    cy, cx = y, x

    for dy, dx, length in directions:
        for _ in range(length):

            if not (0 <= cy < n and 0 <= cx < n):
                return None

            coords.append((cy, cx))

            cy += dy
            cx += dx

    # 한 바퀴 돌았으면 반드시 시작점으로 복귀
    if (cy, cx) != (y, x):
        return None

    return coords


# 시작점 선택
for i in range(n):
    for j in range(n):

        # 우상 / 좌상 확장 범위 설정
        for len_i in range(1, n):
            for len_j in range(1, n):

                coords = get_rectangle(i, j, len_i, len_j)

                if coords is None:
                    continue

                val = 0

                for y, x in coords:
                    val += grid[y][x]

                answer = max(answer, val)


print(answer)