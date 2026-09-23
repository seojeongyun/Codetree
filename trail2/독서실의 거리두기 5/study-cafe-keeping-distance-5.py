# 독서실 사용
    # 이용자들의 좌석 간 거리를 두려고 함
    # 현재 있는 사람들은 원래 자리에 두고, 최대한 거리를 두면서 신규 이용자를 받으려고 함
# 거리: 두 사람이 몇 칸 떨어져 있는지
# 좌석 개수 N개, 공석 여부가 주어지면, 한 명의 인원을 배치한 후 가장 가까운 두 사람 간의 거리를 최대로 하는 프로그램

# 새로 넣은 사람과 기존 사람 간의 거리를 최대로 하는 걸 구했음.
# 문제는 그냥 전체 인원 중 가장 가까운 사람의 거리를 최대로 하고 싶은 거인 거 같음

import sys
input = sys.stdin.readline
answer = -sys.maxsize

N = int(input().strip())
arr = list(map(int, input().strip()))

for i in range(N):
    left_dist, right_dist = sys.maxsize, sys.maxsize
    min_dist = sys.maxsize
    if arr[i] == 0:
        # i랑 가장 가까운 1의 왼쪽 거리 구하기
        for dist, j in enumerate(range(i, -1, -1)):
            if arr[j]:
                left_dist = dist
                break
        
        # i랑 가장 가까운 1의 오른쪽 거리 구하기
        for dist, k in enumerate(range(i, N)):
            if arr[k]:
                right_dist = dist
                break
        
        # 왼쪽 거리와 오른쪽 거리를 비교해서 가장 가까운 거리 구하기
        dist1 = left_dist if left_dist < right_dist else right_dist

        # 기존 사람들 간의 간격
        if sum(arr) > 1:
            for j in range(N):
                for k in range(j+1, N):
                    if arr[j] and arr[k]:
                        dist2 = k-j
                        min_dist = min(min_dist, dist2)
            dist = dist1 if dist1 < min_dist else min_dist
        
        else:
            dist = dist1

        answer = max(answer, dist)

print(answer)