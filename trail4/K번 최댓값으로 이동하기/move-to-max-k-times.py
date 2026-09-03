n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

from collections import deque
# Please write your code here.
def bfs(sr,sc):
    q = deque([(sr,sc)])
    visited = [[0]*n for _ in range(n)]
    visited[sr][sc] = 1
    dr,dc = [-1,1,0,0], [0,0,-1,1]
    start_v = grid[sr][sc]

    best_key = None
    best_position = None

    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr,nc = cr+dr[i], cc+dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
                if grid[nr][nc] < start_v:
                    q.append((nr,nc))
                    visited[nr][nc] = 1

                    cand_key = (-grid[nr][nc], nr, nc)
                    
                    if best_key is None or cand_key < best_key:
                        best_key = cand_key
                        best_position=(nr,nc)
    return best_position

cr,cc = r-1,c-1
for _ in range(k):
    next_position = bfs(cr,cc)
    if next_position is None:
        break
    cr ,cc = next_position

print(cr+1 ,cc+1)
