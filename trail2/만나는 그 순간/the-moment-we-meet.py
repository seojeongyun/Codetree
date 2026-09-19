# A, B가 동일한 시작점에서 출발
# 1초에 1m
# A는 N번, B는 M번 이동
# 최초로 만나게 되는 시간은 몇 초뒤?

import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

# # N이 최대 1천번, t가 최대 1천번이므로, 왼쪽으로 천 번 이동하는 명령어가 천 개 주어질 수 있음.
# # 따라서 배열 개수는 2백만 1개로 선언하고, 1백만에서 출발.
# A = [0] * 2000001
# B = [0] * 2000001

# start = 1000000

# # A와 B의 명령어 분리
# A_cmd = []
# B_cmd = []
# for _ in range(N):
#     A_cmd.append(input().strip().split())

# for _ in range(M):
#     B_cmd.append(input().strip().split())

# # print(A_cmd)
# # A 이동에 따른 A 배열 관리
# A_moved_time = 0
# for dir, time in A_cmd:
#     time = int(time)
#     if dir == 'R':
#         for i in range(start + 1, start + time + 1):
#             A_moved_time += 1
#             A[i] = A_moved_time
#         start = i

#     elif dir == 'L':
#         for i in range(start - 1, start - time - 1, -1):
#             A_moved_time += 1
#             A[i] = A_moved_time
#         start = i

# # print(A)
# start = 1000000
# B_moved_time = 0
# for dir, time in B_cmd:
#     time = int(time)
#     if dir == 'R':
#         for i in range(start + 1, start + time + 1):
#             B_moved_time += 1
#             B[i] = B_moved_time
#         start = i

#     elif dir == 'L':
#         for i in range(start - 1, start - time - 1, -1):
#             B_moved_time += 1
#             B[i] = B_moved_time
#         start = i

# # print(A)
# # print(B)
# # 정답 처리
# for i in range(2000001):
#     if A[i] == B[i] and A[i] != 0:
#         print(A[i])
#         break

# else:
#     print(-1)


# A와 B의 명령어 분리
A_cmd = []
B_cmd = []
for _ in range(N):
    A_cmd.append(input().strip().split())

for _ in range(M):
    B_cmd.append(input().strip().split())

# 명령어 최대 개수 1000개, 한 번의 명령어에서 최대 1000초 이동 가능
# 따라서 MAX_TIME은 1백만, 배열이므로 100만 1.
# 
MAX_TIME = 1000001
A = [sys.maxsize] * MAX_TIME
B = [sys.maxsize] * MAX_TIME

# A 이동에 따른 A 배열 관리
A_position = 0
start = 0
for dir, time in A_cmd:
    time = int(time)
    for i in range(start + 1, start + time + 1):
        if dir == 'R':
            A_position += 1
            A[i] = A_position

        elif dir == 'L':
            A_position -= 1
            A[i] = A_position
    start = i

# B 이동에 따른 B 배열 관리
B_position = 0
start = 0
for dir, time in B_cmd:
    time = int(time)
    for i in range(start + 1, start + time + 1):
        if dir == 'R':
            B_position += 1
            B[i] = B_position

        elif dir == 'L':
            B_position -= 1
            B[i] = B_position
    start = i

for i in range(MAX_TIME):
    if A[i] == B[i] and A[i] != sys.maxsize:
        print(i)
        break

else:
    print(-1)