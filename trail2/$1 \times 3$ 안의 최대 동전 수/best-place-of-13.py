n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
nxn 격자
동전 o 1 x 0
1x3 크기 직사각형 내 동전 개수 최대
    세로 1, 가로 3, 회전 x
'''
ans = -1
for i in range(n):
    for j in range(n):
        if j+2< n and grid[i][j:j+3]:
            ans = max(sum(grid[i][j:j+3]),ans)
print(ans)