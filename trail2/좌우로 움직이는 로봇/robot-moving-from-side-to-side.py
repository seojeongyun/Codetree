# 1차원 직선 위에서 1초에 한 칸 씩 좌우로 움직이는 로봇 A, B
    # A가 움직이는 횟수 N
    # B가 움직이는 횟수 M

# A와 B가 직전에는 서로 다른 위치에 있다가 같은 지점에 위치하는 경우가 몇 번인지 구하시오
    # A = 5, B = 5
    # A = 6, B = 6
    # A = 7, B = 7 .. 이런 경우에는 5 6 7 모두 같은 위치에 있었으므로, 직전에 다른 위치에 있다가 같은 지점에서 위치한다는 규칙에 해당X

# A,B는 처음에 같은 지점에서 움직이며 이는 횟수에 포함 X
# 각 로봇이 움직임을 종료한 이후에는 같은 위치에 머물러 있음
    # 다른 로봇이 움직여 두 로봇이 같은 위치에 존재할 수 있음.
    # A,B의 이동 횟수가 다르다는 말인듯.

import sys
input = sys.stdin.readline
answer = 0

N, M = map(int, input().strip().split())

# 문제에서 이동 거리 합 200만 이하임을 제공
MAX_SIZE = 2000001

# A, B 관리 배열
A = [0] * MAX_SIZE
B = [0] * MAX_SIZE

# A 이동 관리
A_start = 0
for _ in range(N):
    time, dir = input().strip().split()
    for t in range(A_start, A_start+int(time)):
        dist = 1 if dir == 'R' else -1
        A[t] = A[t-1] + dist
    A_start += int(time)

# B 이동 관리
B_start = 0
for _ in range(M):
    time, dir = input().strip().split()
    for t in range(B_start, B_start+int(time)):
        dist = 1 if dir == 'R' else -1
        B[t] = B[t-1] + dist
    B_start += int(time)

# print(*A)
# print(*B)

# 정답 처리: 두 구간으로 분리. 같이 움직이는 구간 + A 혹은 B만 움직이는 구간
min_time = A_start if A_start < B_start else B_start
max_time = A_start if A_start > B_start else B_start

# [1] 같이 움직이는 구간
for i in range(1, min_time+1):
    # 서로 다른 위치에 있다가 동일한 위치로 오게 된 경우만 카운트
    if A[i-1] != B[i-1] and A[i] == B[i]:
        answer += 1

# [2] A 혹은 B만 움직이는 구간
if min_time != max_time:
    for i in range(min_time, max_time+1):
        # A가 B보다 적게 움직인 경우
        if min_time == A_start:
            # A는 정지해있는데, B가 이동하면서 A와 같은 위치에 위치하는 경우
            if A[min_time-1] == B[i]:
                answer += 1

        # B가 A보다 적게 움직인 경우
        elif min_time == B_start:
            # B는 정지해있는데, A가 이동하면서 B와 같은 위치에 위치하는 경우
            if B[min_time-1] == A[i]:
                answer += 1
            
print(answer)