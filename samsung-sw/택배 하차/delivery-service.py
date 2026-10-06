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
def find_bottom(si, sj, ei, ej):
    for i in range(ei, N):
        if sum(arr[i][sj:ej]) != 0:
            return i

    return N
# --------------------------------------------------
def mark(k, si, sj, ei, ej):
    for i in range(si, ei):
        for j in range(sj, ej):
            arr[i][j] = k

# --------------------------------------------------
def drop(k, si, sj, ei, ej):
    sset = set()
    for i in range(si-1, -1, -1):
        for j in range(N):
            if arr[i][j] != 0 and arr[i][j] not in sset: # 아직 처리하지 않은 박스면
                b_num = arr[i][j]
                si, sj, ei, ej = objects[arr[i][j]]
                bottom_i = find_bottom(si, sj, ei, ej)
                n_si, n_ei = si + bottom_i-ei, bottom_i

                mark(0, si, sj, ei, ej)
                mark(b_num, n_si, sj, n_ei, ej)

                objects[b_num] = [n_si, sj, n_ei, ej]
                sset.add(b_num)
# --------------------------------------------------
N, M = map(int, input().strip().split())
obj = [map(int, input().strip().split()) for _ in range(M)]
arr = [[0] * N for _ in range(N)]
#
answer = []
#
objects = {} # obj 좌표 정보 관리
v = [0] * 101

# 택배 좌표 관리할 object 만들기
for k, h, w, c in obj:
    si, sj, ei, ej = 0, c-1, h, c-1+w

    bottom_i = find_bottom(si, sj, ei, ej)
    n_si, n_ei = bottom_i - h, bottom_i
    si, ei = n_si, n_ei

    objects[k] = [si, sj, ei, ej]

    mark(k, si, sj, ei, ej)
    v[k] = 1
    # print_map(arr)

# 택배 하차
left = True
for _ in range(M): # M개 박스
    for num in range(1, 101): # 최대 모든 박스 순회 (작은 박스부터 빼야하니 오름차순)
        if not v[num]: continue

        si, sj, ei, ej = objects[num]

        for i in range(si, ei):
            if left:
                if sum(arr[i][0:sj]) != 0: # 뺄 수 없는 경우
                    break
            else:
                if sum(arr[i][ej:N]) != 0: # 뺄 수 없는 경우
                    break
        else:
            mark(0, si, sj, ei, ej)
            v[num] = 0
            answer.append(num)

            # 여기까지 오면 뺄 수 있는 경우
            drop(num, si, sj, ei, ej)
            # print_map(arr)
            break
    left = not left

print(*answer, sep='\n')