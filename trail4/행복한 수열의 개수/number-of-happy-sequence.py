# 격자 : N x N
    # 1 이상 100 이하의 정수로만 구성

# 행복한 수열: 동일한 원소가 연속하여 M개 이상 나오는 구간이 존재하는 수열

# 2N개의 수열 중 행복한 수열의 개수
    # 2N: 가로로 N개, 세로로 N개

# 제한 조건
# N <= 100 이기 때문에, O(N^4) 이내로만 풀면 됨

import sys
input = sys.stdin.readline

def is_happy_seq(lst):
    for i in range(N):
        compare = [lst[i]]
        for j in range(M):
            # 범위 밖으로 넘어가면 계산 스킵
            if i + j >= N:
                continue
            if compare[0] != lst[i+j]:
                break
            else:
                compare.append(lst[i+j])
        if len(compare) == M+1:
            return 1
    return 0
            
            
# [0] 입력
N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = 0

# [1] 가로 탐색
for i in range(N):
    if is_happy_seq(arr[i]):
        answer += 1

# [2] 세로 탐색
for j in range(N):
    lst = []
    for i in range(N):
        lst.append(arr[i][j])
    if is_happy_seq(lst):
        answer += 1 

print(answer)