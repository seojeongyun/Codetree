n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
nxn 격자 정보/ 동전 O 1 , X 0
격자 벗어나지 않도록 연속한 3개의 행 연속한 3개의 열 이루는
3x3영역 내 들어있는 동전 개수 최대

풀이 방법: nxn 배열에 3x3 필터 순회
'''
coins=0
for ni in range(n):
    for nj in range(n):
        tmp = 0
        for di in range(3):
            for dj in range(3):
                if 0<=ni+di<n and 0<=nj+dj<n:
                    tmp += grid[ni+di][nj+dj]
        coins = max(coins, tmp)
print(coins)

