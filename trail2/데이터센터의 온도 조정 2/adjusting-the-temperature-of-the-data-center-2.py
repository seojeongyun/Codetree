# 어떤 장비가 선호하는 온도 범위의 하한 Ta, 상한 Tb
    # Ta보다 낮으면 작업량은 C
    # Ta 이상 Tb 이하면 작업량은 G
    # Tb보다 높으면 작업량은 H

# 총 작업량은 N개 장비의 작업량을 모두 더한 값

# 장비 개수 N
# 온도에 따른 작업량 C,G,H
# N개 장비가 선호하는 온도 범위

# 온도를 적절히 정했을 때 얻을 수 있는 총 작업량의 최댓값

import sys
input = sys.stdin.readline
answer = -sys.maxsize

N, C, G, H = map(int, input().strip().split())
T = [list(map(int, input().strip().split())) for _ in range(N)]

for temp in range(-1, 1002): # 문제에서 주어진 Ta Tb의 범위가 0 <= Ta <= Tb <= 1000 이므로, -1부터 1001까지 순회
    max_val = 0
    for i in range(N):
        ta, tb = T[i]
        if temp < ta:
            max_val += C
        elif ta <= temp <= tb:
            max_val += G
        elif temp > tb:
            max_val += H
    answer = max(answer, max_val)
print(answer)