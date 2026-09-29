R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
'''
왼상 -> 우하
1. 점프로 이동, 현재 적힌 색과 점프 이후 칸의 색이 달라야함
2. 현재 위치에서 적어도 한칸 이상 오른쪽, 동시에 적어도 한칸 이상 아래쪽으로만 점프 가능
    => 우하 동시 만족해야함
3. 시작, 도착지점 제외 점프하며 도달한 위치가 2곳 뿐
'''


ans = 0

for r1 in range(1, R - 1):
    for c1 in range(1, C - 1):
        if grid[0][0] == grid[r1][c1]:
            continue

        for r2 in range(r1 + 1, R - 1):
            for c2 in range(c1 + 1, C - 1):
                if (grid[r1][c1] != grid[r2][c2]
                        and grid[r2][c2] != grid[R - 1][C - 1]):
                    ans += 1

print(ans)