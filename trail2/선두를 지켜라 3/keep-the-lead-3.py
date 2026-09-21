# A, B가 동일 시작점에서 같은 방향으로 출발
    # 도중에 방향 바꾸는 경우 X
    # A는 N개 명령어
    # B는 M개 명령어

# 명령어
    # 어떤 속도로 몇 시간 이동했는지 나타내는 v, t

# 명예의 전당
    # 매 시간마다 가장 앞서있는 사람들을 모아 명예의 전당에 이름을 올림
    # 두 사람의 위치가 같으면 둘 다 올라감
    # 처음에 비어있음
    # 1시간 간격으로 그 시점의 선두 조합을 기록
    # 새로 기록한 조합이 직전 기록 조합과 다르면 조합이 한 번 바뀐 것
    # 첫 기록은 항상 한 번 바뀐것으로 간주

# A의 총 이동 시간 == B의 총 이동 시간

# 선두 조합이 몇 번 바뀌었는지 출력

import sys
input = sys.stdin.readline
answer = 1 # 첫 기록은 항상 한 번 바뀐 것으로 간주하기에 answer는 1부터 시작

N, M = map(int, input().strip().split())

# 명령어 개수 1,000 * 시간 1,000
MAX_SIZE = 1000001
A = [0] * MAX_SIZE
B = [0] * MAX_SIZE

# A 이동 관리
A_time = 0 # offset
for _ in range(N):
    v, t = map(int, input().strip().split())
    for time in range(1, t+1):
        A[A_time + time] = A[A_time + time-1] + v
    A_time += time

# B 이동 관리
B_time = 0 # offset
for _ in range(M):
    v, t = map(int, input().strip().split())
    for time in range(1, t+1):
        B[B_time + time] = B[B_time + time-1] + v
    B_time += time

lst = []
for i in range(A_time+1):
    if A[i] > B[i]:
        lst.append('A')
    elif A[i] < B[i]:
        lst.append('B')
    else:
        lst.append('AB')

# A[0], B[0]은 0이기 때문에, 이 기록은 포함하지 않기 위해 2부터 시작
for i in range(2, A_time+1):
    if lst[i-1] != lst[i]:
        answer += 1

print(answer)
