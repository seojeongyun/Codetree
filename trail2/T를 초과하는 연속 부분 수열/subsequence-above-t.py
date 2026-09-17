# N개의 수로 구성된 수열 정보와 정수 T가 주어짐
# T보다 큰 수로만 이루어진 연속 부분 수열중 최대 길이

import sys
input = sys.stdin.readline

N, T = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

max_len = 0
answer = 0
for i in range(N):
    if arr[i] > T:
        max_len += 1
    else:
        max_len = 0
    answer = max(answer, max_len)

print(answer)