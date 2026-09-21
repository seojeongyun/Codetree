# A, B가 동일한 시작점에서 같은 방향으로 출발
    # 도중에 방향 바꾸는 경우 X
    # A는 N번 특정속도로 특정 시간 이동
    # B는 M번 특정속도로 특정 시간 이동

# 선두가 몇 번 바뀌는지 출력
# 두 사람이 공동으로 선두를 지키는 경우는 선두가 바뀌었다고 판단 X
# A와 B의 총 이동 시간은 항상 동일

import sys
input = sys.stdin.readline
answer = 0

N, M = map(int, input().strip().split())

# 명령어 개수 1,000개 * t 최대 1,000 = 1,000,000
MAX_SIZE = 1000001

# 배열 생성: idx는 시간, value는 총 이동 거리
A = [0] * MAX_SIZE
B = [0] * MAX_SIZE

# A의 이동 관리
# offset 역할
A_start = 0 
for _ in range(N):
    v, t = map(int, input().strip().split())
    for time in range(1, t+1):
        A[A_start+time] = A[A_start+time-1] + v
    A_start += t

# B의 이동 관리
B_start = 0 # offset 역할
for _ in range(M):
    v, t = map(int, input().strip().split())
    for time in range(1, t+1):
        B[B_start+time] = B[B_start+time-1] + v
    B_start += t

# print(A)
# print(B)

# 정답 처리: A_start가 total time을 내포함.
# 선두가 바뀌는 경우에 대해서만 처리
# 초기 등수 결정에 대해서는 배제해야함. 1 빼줌.
for i in range(1, A_start+1):
    if A[i-1] >= B[i-1] and A[i] < B[i]:
        # print('if:', i)
        answer += 1
    elif A[i-1] <= B[i-1] and A[i] > B[i]:
        # print('elif:', i)
        answer += 1

print(answer-1)