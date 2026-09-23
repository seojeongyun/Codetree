n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = 0
def get_rectangle(i,j,leni,lenj):
    cy,cx = i,j
    coords = []
    directions = [(-1,1,leni), # 우상
                  (-1,-1,lenj), # 좌상
                  (1,-1,leni), #좌하
                  (1,1,lenj)  # 우하
                   ] 
    for dy,dx,length in directions:
        for _ in range(length):

            if not(0<=cy<n and 0<=cx<n):
                continue
            
            coords.append((cy,cx))
            cy += dy
            cx += dx
    if (cy,cx) == (i,j):
        return coords


# 시작점 순회
for i in range(n):
    for j in range(n):
        # 마름모 크기 순회
        for leni in range(1,n):
            for lenj in range(1,n):
                coords = get_rectangle(i,j,leni,lenj)
                if coords:
                    val = 0
                    for y,x in coords:
                        val += grid[y][x]
                    ans = max(ans,val)
print(ans)