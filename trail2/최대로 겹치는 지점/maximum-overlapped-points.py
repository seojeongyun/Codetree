# 끝점에서 닿는 경우도 덮는 것으로 간주하기 때문에, 구간 전 범위에 대해 +1씩 누적

import sys
input = sys.stdin.readline

N = int(input().strip())
x1x2 = [list(map(int, input().strip().split())) for _ in range(N)]

arr = [0] * 101
for x1, x2 in x1x2:
    for i in range(x1, x2+1):
        arr[i] += 1

print(max(arr))