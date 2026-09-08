n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
'''
1~100이하 정수 NxN
행복한 수열 = 동일 원소 연속 M개 나오는 구간 존재

1xN, Nx1로 얻어지는 2N개의 수열 중
행복한 수열 개수 출력
'''
happy = 0
# 완전 탐색
def find_happy(arr):
    cnt = 1
    # 원소 하나만 연속해도 행복한 수열
    if m == 1:
        return 1
        
    for i in range(1,n):
        if arr[i] == arr[i-1]:
            cnt+=1
        else:
            cnt=1
        
        if cnt >= m:
            return 1
    return 0

# row에서 연속된 수 찾기
for i in range(n):
    row = grid[i]
    happy += find_happy(row)


# col에서 연속된 수 찾기
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    happy += find_happy(col)

print(happy)
