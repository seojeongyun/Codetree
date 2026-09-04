import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(cr, cc, k):
    visited[cr][cc] = 1

    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            # 방문하지 않았고, 물에 잠기지 않은 집
            if not visited[nr][nc] and grid[nr][nc] > k:
                dfs(nr, nc, k)


max_height = max(map(max, grid))

answer_k = 1
max_safe_count = 0

for k in range(1, max_height + 1):

    # K가 바뀌면 방문 기록도 초기화
    visited = [[0] * m for _ in range(n)]

    safe_count = 0

    for r in range(n):
        for c in range(m):

            # 잠기지 않았고 아직 방문하지 않은 집
            if grid[r][c] > k and not visited[r][c]:
                dfs(r, c, k)

                # 새로운 안전 영역 하나를 발견
                safe_count += 1

    # 안전 영역이 더 많을 때만 갱신
    if safe_count > max_safe_count:
        max_safe_count = safe_count
        answer_k = k

print(answer_k, max_safe_count)