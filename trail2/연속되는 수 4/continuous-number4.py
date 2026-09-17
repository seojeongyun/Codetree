# N개의 정수로 이루어진 수열
# 증가하는 연속 부분 수열 중 최대 길이

import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

max_val = -sys.maxsize
answer = 0
for i in range(N):
    if i > 0 and (arr[i] > arr[i-1]):
        max_val += 1
    else:
        max_val = 0 

    answer = max(max_val, answer)

print(answer+1)
