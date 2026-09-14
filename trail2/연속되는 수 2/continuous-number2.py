# N개의 정수가 주어졌을 때 같은 정수가 연속해서 나오는 횟수 중 최댓값

import sys
input = sys.stdin.readline

N = int(input().strip())
lst = [int(input().strip()) for _ in range(N)]

cnt = 0
answer = -sys.maxsize
for i in range(N):
    if i > 0 and lst[i] == lst[i-1]:
        # print(lst[i])
        cnt += 1
    else:
        cnt = 0
    answer = max(answer, cnt)

print(answer+1)