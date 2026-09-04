n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
nxn, 사람 1 or 벽 0
인접한 영역에 있는 사람 = 같은 마을

1: 총 마을 개수
각 마을 내 사람 수 오름차순 / 한 줄에 하나씩
'''

visited = [[0]*n for _ in range(n)]
ans = []
def dfs(ci,cj):
    visited[ci][cj] = 1
    cnt = 1

    di, dj = [-1,1,0,0], [0,0,-1,1]
    for i in range(4):
        ni,nj = ci+di[i], cj+dj[i]
        if 0<=ni<n and 0<=nj<n and not visited[ni][nj]:
            if grid[ni][nj]:
                cnt +=  dfs(ni,nj)

    return cnt


for i in range(n):
    for j in range(n):
        # 새로운 마을 발견한 경우에만 dfs실행
        if grid[i][j]==1 and not visited[i][j]:
            humans = dfs(i,j)
            ans.append(humans)

ans.sort()
print(len(ans))
for i in ans:
    print(i)

    
