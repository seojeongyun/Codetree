# 격자: N x M
    # 각 영역에 자연수 존재
# ㄴ, ㅡ(1x3) 모양의 블럭을 올려놓아 블럭 내에 적힌 수의 합이 최대가 되는 경우 구하기
    # ㄴ, ㅡ 모양은 자유롭게 회전하거나 뒤집을 수 있다.

import sys
input = sys.stdin.readline

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = -sys.maxsize

# 블럭의 좌상단 지점(i, j)
for i in range(N):
    for j in range(M):
        # ㄴ 블럭의 탐색 범위
        # 회전 X:             (i, j), (i+1, j), (i+1, j+1)
        sum_val = 0
        if in_range(i+1, j+1):
            sum_val = arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
        answer = max(answer, sum_val)

        # 오른쪽으로 90도 회전:  (i, j), (i, j+1), (i+1, j)
        sum_val = 0
        if in_range(i+1, j+1):
            sum_val = arr[i][j] + arr[i][j+1] + arr[i+1][j]
        answer = max(answer, sum_val)

        # 오른쪽으로 180도 회전: (i, j), (i, j+1), (i+1, j+1)
        sum_val = 0
        if in_range(i+1, j+1):
            sum_val = arr[i][j] + arr[i][j+1] + arr[i+1][j+1]
        answer = max(answer, sum_val)

        # 오른쪽으로 270도 회전: (i, j+1), (i+1, j), (i+1, j+1)
        sum_val = 0
        if in_range(i+1, j+1):
            sum_val = arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1]
        answer = max(answer, sum_val)


        # ㅡ 블럭의 탐색 범위
        # 회전 X: (i, j), (i, j+1), (i, j+2)
        sum_val = 0
        if in_range(i, j+2):
            sum_val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        answer = max(answer, sum_val)

        # 회전 O: (i, j), (i+1, j), (i+2, j)
        sum_val = 0
        if in_range(i+2, j):
            sum_val = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        answer = max(answer, sum_val)

print(answer)
