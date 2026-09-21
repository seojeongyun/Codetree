# A, B가 동일한 시작점에서 출발
    # 1초에 1m 이동
# 명령어
    # 방향, 시간이 주어짐.
        # R 5 면 오른쪽으로 5m 이동, 5초 소요
    # A는 N개의 명령어
    # B는 M개의 명령어
    # 이동 시간은 항상 동일
    # 처음 이동 방향은 서로 다름
# A,B가 최초로 만나게 되는 시간은 몇 초 뒤인가

import sys
input = sys.stdin.readline

# 1,000개의 명령어가 주어지고, 한 명령어당 1,000초 이동 가능하므로, 1,000*1,000 = 1,000,000
MAX_SIZE = 1000001

N, M = map(int, input().strip().split())
A = [0] * MAX_SIZE
B = [0] * MAX_SIZE

# A 이동 관리
A_start = 0
total_time = 0
for _ in range(N):
    dir, time = input().strip().split()
    total_time += int(time)
    for t in range(A_start, A_start+int(time)):
        if dir == 'R':
            A[t] = A[t-1] + 1
        else:
            A[t] = A[t-1] - 1
    A_start += int(time)

# B 이동 관리
B_start = 0
for _ in range(M):
    dir, time = input().strip().split()
    for t in range(B_start, B_start+int(time)):
        if dir == 'R':
            B[t] = B[t-1] + 1
        else:
            B[t] = B[t-1] - 1
    B_start += int(time)

# print(A)
# print(B)
# print(A[990:1001])
# print(B[990:1001])
# A, B 만나는 위치 확인
for i in range(1, total_time):
    if A[i] == B[i]:
        print(i+1)
        break
else:
    print(-1)