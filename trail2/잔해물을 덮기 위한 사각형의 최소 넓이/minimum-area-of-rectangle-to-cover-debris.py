# 첫 번째 직사각형이 놓여있고, 두 번째 직사각형이 그 다음에 놓인다.
    # 첫 번째 직사각형이 두 번째 직사각형에 의해 가려짐.
# 남아있는 첫 번째 직사각형을 덮기 위한 최소 직사각형의 넓이

import sys
input = sys.stdin.readline
answer = 0

# (x1, y1, x2, y2): 1은 좌하단 2는 우상단
rect_coords = [list(map(int, input().strip().split())) for _ in range(2)]

# -1000부터 1000까지니까, 2001
MAX = 2001
OFFSET = 1000
arr = [[0] * MAX for _ in range(MAX)]

for idx, (x1, y1, x2, y2) in enumerate(rect_coords):
    x1, y1, x2, y2 = x1+OFFSET, y1+OFFSET, x2+OFFSET, y2+OFFSET
    for i in range(y1, y2):
        for j in range(x1, x2):
            rect_num = idx +1
            arr[i][j] = rect_num

min_i, max_i, min_j, max_j = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize

# for row in arr:
#     print(*row)

for i in range(MAX):
    for j in range(MAX):
        if arr[i][j] == 1:
            min_i = min(min_i, i)
            max_i = max(max_i, i)
            min_j = min(min_j, j)
            max_j = max(max_j, j)

# print(max_i, min_i, max_j, min_j)
if min_i == sys.maxsize and max_i == -sys.maxsize and min_j == sys.maxsize and max_j == -sys.maxsize:
    print(0)
else:
    print((max_i-min_i+1) * (max_j-min_j+1))
