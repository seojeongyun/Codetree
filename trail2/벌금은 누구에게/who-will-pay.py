# N명의 학생
    # 1번부터 N번까지 번호가 붙여져 있음
# 한 학생이 K 번 이상 벌칙을 받게 되면 벌금을 내야함.
# M번에 걸쳐 벌칙에 걸린 학생 번호가 주어질 때, 최초로 벌금을 내는 학생은?

import sys
input = sys.stdin.readline

N, M, K = map(int, input().strip().split())
NUM = [int(input().strip()) for _ in range(M)]

arr = [0] * (N+1)
for i in NUM:
    arr[i] += 1
    if arr[i] >= K:
        print(i)
        break
else:
    print(-1)