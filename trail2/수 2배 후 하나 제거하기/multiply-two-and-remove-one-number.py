# 정수 N개로 이루어진 수열
# 원소 하나를 골라 2배로 만든 후, 원소 하나를 골라 제거
# 남은 N-1개의 원소는 원래 순서를 유지
# 점수: 인접한 두 원소마다 차의 절댓값을 구해 모두 더한 값
# 점수가 가장 작아지도록 두 원소를 고를 때, 점수의 최솟값을 구하시오

import sys
input = sys.stdin.readline
answer = sys.maxsize

N = int(input().strip())
seq = list(map(int, input().strip().split()))

# 2배 할 원소 고르는 for문
for i in range(N):
    # 제거할 원소 고르는 for문
    for j in range(N):
        # 
        lst = seq[::]
        lst[i] = lst[i] * 2
        score = 0
        lst.pop(j)
        for k in range(1, N-1):
            score += abs(lst[k-1] - lst[k])
        answer = min(answer, score)

print(answer)