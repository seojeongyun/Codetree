# 격자: N x N
    # 0은 빈칸, 1은 채워진 칸

# 1 x M 크기 블럭이 가장 위에서부터 떨어짐
# 블럭이 떨어지는 도중 한 곳에라도 바닥 혹은 이미 놓여있던 블럭과 맞닿게 되면 멈춤
# 떨어진 이후의 상태를 출력하는 프로그램

def find_i():
    for i in range(N):
        for j in coords_j:
            if arr[i][j] != 0:
                return i-1

    return -1
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# K번째 열부터 K+M-1열까지 공간 차지
coords_j = [i for i in range(K-1, K+M-1)]
i = find_i()

if i != -1: # 바닥
    for j in coords_j:
        arr[i][j] = 1

else: # 다른 블럭
    for j in coords_j:
        arr[N-1][j] = 1
        
for row in arr:
    print(*row)
