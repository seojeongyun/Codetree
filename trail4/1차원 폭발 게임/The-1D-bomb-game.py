# N개의 폭탄
# M개 이상 연속으로 같은 정수가 적힌 폭탄은 터짐
# 이후 중력에 의해 남아있던 폭탄들이 아래로 떨어짐

import sys

input = sys.stdin.readline


def drop():
    tmp_arr = []

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > 0:
            tmp_arr.append(arr[i])

    arr[:] = tmp_arr[::-1]


def boom():
    for lst in bomb_lst:
        for i in lst:
            arr[i] = 0


def check():
    lst = []
    v_lst = [arr[0]]
    coords = [0]

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            v_lst.append(arr[i])
            coords.append(i)
        else:
            if len(v_lst) >= M:
                lst.append(coords)
            v_lst = [arr[i]]
            coords = [i]
    
    # 마지막 연속 구간 검사
    if len(v_lst) >= M:
        lst.append(coords)
        
    return lst


N, M = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]

while True:
    valid = False
    if len(arr) > 0:
        bomb_lst = check()

    else:
        break
        
    if len(bomb_lst) > 0:
        boom()
        valid = True

    if valid:
        drop()

    if not valid:
        break

print(len(arr))
if len(arr) > 0:
    for i in arr:
        print(i)


