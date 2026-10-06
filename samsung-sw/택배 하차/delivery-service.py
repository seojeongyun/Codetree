# 격자: N x N

# [1] 택배 투입
    # 택배는 직사각형 모양
        # 왼쪽 열의 위치(c), 가로 크기(w), 세로 크기(h), 번호(k)가 주어짐
    # 중력에 의해 하단으로 떨어짐
        # 바닥으로 닿거나 다른 짐을 만나면 멈춤
# [2] 택배 하차 (좌측)
    # 쌓인 택배 중 잡고 왼쪽으로 이동했을 때 다른 택배와 부딪히지 않고 뺄 수 있는 택배를 먼저 하차
    # 그러한 택배가 여러개인 경우 번호가 작은 택배를 먼저 하차
    # 하차 이후 떨어질 수 있는 것들은 떨어짐

# [3] 택배 하차 (우측)
    # 2의 과정 진행

# 공간에 있는 택배를 모두 하차할 때 까지 2, 3의 과정 반복

# 하차되는 택배의 번호를 순서대로 출력하는 프로그램 작성

import sys
input = sys.stdin.readline

def print_map(arr):
    for row in arr:
        print(' '.join(f'{x:2}' for x in row))
    print('--------------')
# --------------------------------------------------
def in_range(i, j):
    return 0 <= i < N and 0 <= j < N
# --------------------------------------------------
def is_done(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                return False
    return True
# --------------------------------------------------
def drop(objects):
    for k in list(objects.keys()):
        stop = False
        k, coords, h, w, c = objects[k]
        if coords == [-1, -1]: continue
        for d_cnt in range(1, N+1):  # 떨어트릴 칸 수
            for ci, cj in coords[:w]: # 가장 아래 행만 떨어트림
                ni, nj = ci+d_cnt, cj
                if ni == N or arr[ni][nj] != 0:
                    stop = True
                    break
            if stop:
                for idx, (i, j) in enumerate(objects[k][1]):
                    arr[i][j] = 0
                    arr[i+d_cnt-1][j] = k   # arr에 표시
                    objects[k][1][idx] = [i + d_cnt-1, j] # d_cnt-1만큼 더한 값으로 objects 좌표 갱신

                break

    return arr, objects
# --------------------------------------------------
def clear(arr, objects, dir_num):
    out_of_range = N if dir_num == 0 else -1

    # objects key를 오름차순으로 sort
    objects_order = sorted(list(objects.keys()))

    for num in objects_order: # k가 작은 순서부터 접근
        next_obj = False
        if objects[num][1] == [-1, -1]: continue
        # 모든 좌표가 중간에 걸리지 않고 나올 수 있는가?
        for ci, cj in objects[num][1]:
            for shift_num in range(1, N+1):
                ni = ci
                nj = cj + shift_num if dir_num == 0 else cj - shift_num
                #
                if nj == out_of_range or arr[ni][nj] == num: break
                if arr[ni][nj] != 0:
                    next_obj = True
                    break
            if next_obj:
                break
        # 모든 좌표가 걸리지 않고 나왔다면
        else:
            # arr에서 해당 택배 제거
            for ci, cj in objects[num][1]:
                arr[ci][cj] = 0

            # 해당 택배가 없음을 의미하도록 좌표 대신 -1
            objects[num][1] = [-1, -1]
            answer.append(num)
            return arr, objects, False

    return arr, objects, True
# --------------------------------------------------
N, M = map(int, input().strip().split())
obj = [map(int, input().strip().split()) for _ in range(M)]
arr = [[0] * N for _ in range(N)]
n_arr = [[0] * N for _ in range(N)]
answer = []
#
objects = {} # obj 좌표 정보 관리

# 택배 좌표 관리할 object 만들기
for k, h, w, c in obj:
    object = list()                                     # 일단 list로 만들고, 시간 부족하면 set으로 수정
    ci, cj = 0, c-1

    # arr에 택배 초기 위치 표기
    for i in range(h-1, -1, -1):
        for j in range(cj, cj+w):
            object.append([i, j])
    objects[k] = [k, object, h, w, c]

# 하차 시뮬레이션 시작
dir_num = 2
while True:
    # 종료 조건
    # if is_done(arr):
    #     break

    # 택배 떨어트리기
    arr, objects = drop(objects)
    # print_map(arr)

    # 택배 하차, dir로 컨트롤
    arr, objects, is_done = clear(arr, objects, dir_num)
    dir_num = (dir_num + 2) % 4
    # print_map(arr)

    if is_done:
        break

print(*answer, sep='\n')