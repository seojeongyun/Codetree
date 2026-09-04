n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
좌상단 시작 ->아래,오른쪽으로만 이동 가능
뱀있는곳 = 이동 x= 0
'''

visited = [[0]*m for _ in range(n)]
def dfs(cx,cy):
    global cnt
    dx,dy = [1,0],[0,1]

    if cx==m-1 and cy ==n-1:
        return 1

    for i in range(2):
        nx,ny = cx+dx[i] , cy+dy[i]
        if 0<=nx<m and 0<=ny<n and not visited[ny][nx]:
            if grid[ny][nx]:
                visited[ny][nx] = 1
                if dfs(nx, ny):
                    return 1
                dfs(nx,ny)
                
    return 0

print(dfs(0,0))
