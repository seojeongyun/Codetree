# 0이 아닌 N개의 정수 중 부호가 동일한 정수로만 이루어진 연속 부분 수열 중 최대 길이

import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
answer = 0
length = 0

for i in range(N):
    if i > 0 and ((arr[i] > 0 and arr[i-1] > 0) or (arr[i] < 0 and arr[i-1] < 0)):
        # print(arr[i])
        length += 1
    else:
        length = 0
    answer = max(answer, length)

print(answer+1)