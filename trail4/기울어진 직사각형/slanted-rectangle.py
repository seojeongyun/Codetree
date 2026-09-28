# 격자: N x N
# 기울어진 직사각형
    # 격자 내 한 지점으로부터 대각선으로 움직이며 반시계 방향 순회
    # 1,2,3,4번 방향순으로 순회해야하며 각 방향으로 최소 1번 움직여야함
    # 이동 중 격자 밖으로 넘어가선 안됨

# 핵심 아이디어: 완전탐색
    # 각 방향에 대해 완전탐색 진행
        # 이동 중 격자 밖으로 이탈하면 해당 방향으로 이동하기 전의 위치로 복귀 (좌표 관리)
        # 모든 이동에 대해 격자 이탈이 없었다면, 평행하는 방향의 길이가 같은 경우 정답 처리

def in_range(i, j):
    return 0 <= i < N and 0 <= j < N

def rect(ci, cj, length_i, length_j):
    # k는 dir_num 0, 2인 경우
    # l은 dir_num 1, 3인 경우

    val = 0
    
    for length, dir in ((length_i, 0), (length_j, 1), (length_i, 2), (length_j, 3)):
        for _ in range(length):
            dir_num = dir
            ni, nj = ci+di[dir_num], cj+dj[dir_num]

            if not in_range(ni, nj):
                return -1

            val += arr[ni][nj]
            ci, cj = ni, nj

    return val
        
import sys

input = sys.stdin.readline
answer = 0

# 입력
N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# di, dj, dir_num
di, dj = (-1, -1, 1, 1), (1, -1, -1, 1)

for row in range(N):
    for col in range(N):
        ci, cj = row, col

        # 각 변의 길이
        for length_i in range(1, N+1): # / 방향: dir_num 0, 2
            for length_j in range(1, N+1): # \ 방향: dir_num 1, 3
        
                val = rect(ci, cj, length_i, length_j)

                if val == -1: # 격자 이탈 시 -1을 return하는데, 이 경우 다음 length_j로 넘어가도록 continue
                    continue

                answer = max(answer, val)

print(answer)
                    
