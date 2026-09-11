# 좌표평면 위에 직사각형 A,B를 올린 뒤 M을 올림
    # M에 의해 A,B 일부가 가려짐
# M으로 덮이지 않은 직사각형 A,B의 넓이의 합

# A, B 직사각형을 1로 표시
# M을 0으로 표시
# 격자 전체 순회하며 1의 개수 세기

import sys
input = sys.stdin.readline

# (x1, y1, x2, y2)
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
M = list(map(int, input().strip().split()))

# -1000 <= x,y <= 1000
arr = [[0] * 2001 for _ in range(2001)]

answer = 0

x1, y1, x2, y2 = A
for i in range(y1, y2):
    for j in range(x1, x2):
        arr[i][j] = 1

x1, y1, x2, y2 = B
for i in range(y1, y2):
    for j in range(x1, x2):
        arr[i][j] = 1

x1, y1, x2, y2 = M
for i in range(y1, y2):
    for j in range(x1, x2):
        arr[i][j] = 0

for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            answer += 1

print(answer)

