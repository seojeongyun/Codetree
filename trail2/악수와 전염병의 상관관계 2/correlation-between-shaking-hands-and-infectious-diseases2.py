# N명의 개발자, T개의 악수 기록
    # 어떤 두 개발자가 몇 초에 악수를 나눴는지를 의미

# 전염병 옮김
    # 처음에는 P번 개발자 한 명만 전염병에 감염되어 있음
        # 전염병을 옮길 수 있는 악수는 K번 남음
    # 어떤 개발자가 감염되면 k번 악수 동안 전염병을 옮길 수 있음.

# 전염 가능한 상태
    # 어떤 개발자가 감염되어 있고 남은 전염 횟수가 1번 이상인 상태

# 악수 처리
    # 시각이 이른 것 부터
    # 악수에 참여한 두 개발자 각각에 대해, 그 개발자가 전염 가능한 상태였다면 남은 전염 횟수 1 줄어듦 (둘 다 전가상이면 각각 1회 차감)
    # 한 쪽만 전가상이고 다른 쪽이 감염되어있지 않았으면, 다른 쪽은 감염되고 감염횟수 K번을 받음

# 최종적으로 누가 전염병에 걸렸는지 알아내는 프로그램 작성

import sys
input = sys.stdin.readline

# [1] 데이터 입력 받기
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
N, K, P, T = map(int, input().strip().split())

# ti, xi, yi = ti초에 xi번과 yi번이 악수를 나눴음을 의미
handshakes = [list(map(int, input().strip().split())) for _ in range(T)]
# -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*


# [2] 각 개발자의 상태를 배열로 관리
    # 감염 여부, 남은 횟수
developers = []
for i in range(1,N+1):
    if i == P:
        developers.append([1, K])
    else:
        developers.append([0, 0])


# [3] 악수 처리: 시각이 이른 것 부터 처리해야하므로 시간 기준 sorting
# 누구누구가 악수했는지가 감염 여부를 따지는 거니까 ti가 갖는 의미는 없는 거 같음. 그냥 sorting 기준인듯?
handshakes.sort(key=lambda x: x[0])
# 순차적으로 악수 처리
for t, x, y in handshakes:
    x_is_infection, x_count = developers[x-1]
    y_is_infection, y_count = developers[y-1]
    
    # 만약 x나 y중 감염자가 있었다면, 감염 여부 및 남은 횟수 갱신
    # x만 감염자인지, y만 감염자인지, x-y 모두 감염자인지에 따라 달라짐
    if x_is_infection and not y_is_infection: # x만 감염자
        developers[x-1] = [x_is_infection, x_count-1]
        if x_count > 0:
            developers[y-1] = [1, K]

    elif y_is_infection and not x_is_infection:
        developers[y-1] = [y_is_infection, y_count-1]
        if y_count > 0:
            developers[x-1] = [1, K]

    elif x_is_infection and y_is_infection:
        developers[x-1] = [x_is_infection, x_count-1]
        developers[y-1] = [y_is_infection, y_count-1]


for developer in developers:
    print(developer[0], end='')