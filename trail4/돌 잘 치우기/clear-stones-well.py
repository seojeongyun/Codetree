from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

start_positions = []

for _ in range(k):
    row, col = map(int, input().split())
    start_positions.append((row - 1, col - 1))


# 모든 돌의 좌표
stones = []

for row in range(n):
    for col in range(n):
        if grid[row][col] == 1:
            stones.append((row, col))


def bfs(removed_stones):
    removed_set = set(removed_stones)

    visited = [[False] * n for _ in range(n)]
    q = deque()

    # 모든 시작점을 큐에 삽입
    for start_row, start_col in start_positions:
        if not visited[start_row][start_col]:
            visited[start_row][start_col] = True
            q.append((start_row, start_col))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    count = len(q)

    while q:
        current_row, current_col = q.popleft()

        for direction in range(4):
            next_row = current_row + dr[direction]
            next_col = current_col + dc[direction]

            if 0 <= next_row < n and 0 <= next_col < n:
                if not visited[next_row][next_col]:

                    # 원래 빈칸이거나 제거하기로 선택한 돌
                    can_move = (
                        grid[next_row][next_col] == 0
                        or (next_row, next_col) in removed_set
                    )

                    if can_move:
                        visited[next_row][next_col] = True
                        q.append((next_row, next_col))
                        count += 1

    return count


answer = 0

# 제거할 돌 M개의 모든 조합 확인
for removed_stones in combinations(stones, m):
    reachable_count = bfs(removed_stones)
    answer = max(answer, reachable_count)

print(answer)