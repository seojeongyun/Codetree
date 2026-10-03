# 격자: N x N

# 각 열 기준으로 연속으로 M개 이상 같은 숫자가 적혀있는 폭탄이 터짐
# 이후 중력에 의해 남은 폭탄들이 떨어짐

import sys

input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))

def check():
    lst = []
    for j in range(N):
        start = 0
        for i in range(1, N+1):
            if i == N or arr[i][j] != arr[start][j]:
                if arr[start][j] != 0 and i - start >= M:
                    lst.append([(r, j) for r in range(start, i)])
                start = i
    return lst


def boom(bomb_lst):
    for lst in bomb_lst:
        for i, j in lst:
            arr[i][j] = 0


def drop():
    global arr
    new_arr = [[0] * N for _ in range(N)]

    for j in range(N):
        cnt = 0
        for i in range(N - 1, -1, -1):
            if arr[i][j]:
                new_arr[N - 1 - cnt][j] = arr[i][j]
                cnt += 1

    # for i in range(N):
    #     for j in range(N):
    #         arr[i][j] = new_arr[i][j]
    arr = new_arr


def rotate():
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[N - 1 - j][i]

    for i in range(N):
        for j in range(N):
            arr[i][j] = new_arr[i][j]
    return


N, M, K = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = 0

if N == 1 and M == 1:
    print(0)

elif N == 1 and M > 1:
    print(1)
    
else:
    for _ in range(K+1):
        while True:
            # 체크
            bomb_lst = check()
            # print(bomb_lst)

            if len(bomb_lst) > 0:
                # 폭발
                boom(bomb_lst)
                # print('---bomb---')
                # print_map(arr)

                # 중력
                drop()
                # print('---drop---')
                # print_map(arr)

            else:
                break

        # 회전
        rotate()
        # print('---rotate---')
        # print_map(arr)

        # 중력
        drop()
        # print('---drop---')
        # print_map(arr)

    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                answer += 1

    print(answer)