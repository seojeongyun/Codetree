# 격자: NxN
    # 1: 동전 있는 곳
    # 0: 동전 없는 곳

# 3X3 크기의 격자를 잡아, 해당 범위 내에 들어있는 동전의 개수를 최대로 하는 프로그램

# 시간 제한: 1초
# 메모리: 64MiB

import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = -sys.maxsize

# for si in range(N-2):
#     for ei in range(si, si+3):
#         for sj in range(N-2):
#             for ej in range(sj, sj+3):

answer = -sys.maxsize

for j in range(N-2):
    for i in range(N-2):
        max_val = 0
        for k in range(3):
            max_val += sum(arr[i+k][j:j+3])
        answer = max(answer, max_val)

print(answer)