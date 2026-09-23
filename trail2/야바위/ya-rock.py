# 3개의 종이컵이 1번, 2번, 3번에 위치
# N번의 연산
    # a번과 b번을 서로 맞바꾼 뒤, c번에 조약돌이 있으면 1점
# 조약돌을 어느 종이컵 아래에 넣어야 최대 점수를 얻을 수 있나

import sys
input = sys.stdin.readline
answer = 0 

N = int(input().strip())
cmd = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(1, 4):
    arr = [0] * 4
    arr[i] = 1  # i번 종이컵에 조약돌 넣기
    score = 0
    for a, b, c in cmd:
        # a-b swap
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
        
        # c번에 조약돌 있으면 1점
        if arr[c]:    
            score += 1

    answer = max(answer, score)

print(answer)