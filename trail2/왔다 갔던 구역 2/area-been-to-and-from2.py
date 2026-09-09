# 수직선 위치 0에서 시작해 N번의 명령에 걸쳐 움직인 뒤, 2번 이상 지나간 영역의 크기를 출력

# 명령
    # "x L": 왼쪽으로 x만큼
    # "x R": 오른쪽으로 x만큼 이동해야 함
    # 왼쪽으로 이동하는 경우에는 음수 처리에 유의해야 할듯
# 영역의 크기는 길이로 센다.
    # k와 k+1 사이의 길이 1인 구간을 단위로 보고 그 단위 구간을 2번 이상 지나간 것의 개수가 답

# 갔다가 와야 하나를 카운트하는 구조.
# 이전 문제들은 주어진 구간에 대해 겹치는 부분만 구하면 됐는데, 갔
import sys
input = sys.stdin.readline

N = int(input().strip())
min_val = sys.maxsize
answer = 0
sum_val = 0
cx = 0
cmd = []
arr = [0] * 1001
dir_arr = [[] for _ in range(1001)]

for _ in range(N):
    x, dir = input().strip().split()
    if dir == 'R':
        sum_val += int(x)
    else:
        sum_val -= int(x)
    min_val = min(min_val, sum_val)
    cmd.append([int(x), dir])

cx = cx - min_val
for x, dir in cmd:
    # 현재 위치 저장 해두고 +x만큼 범위 설정
    if dir == 'R':
        # print(range(cx, cx+x))
        for i in range(cx, cx+x):
            arr[i] += 1
            dir_arr[i].append(dir)
        cx = cx+x
    else:
        # print(range(cx, cx-x))
        for i in range(cx-1, cx-x-1, -1):
            arr[i] += 1
            dir_arr[i].append(dir)
        cx = cx -x

# print(arr)
for i in range(len(arr)):
    # if arr[i] >= 2 and len(set(dir_arr[i])) == 2:
    if arr[i] >= 2:
        answer += 1

# print(arr)
# print(dir_arr)
print(answer)


'''
    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
                           1  1
                    1 1 1  1  1  1
                  1
      1 1 1 1 1 1 1 1
    1
      1 1
    1 2 2 1 1 1 1 2 2 1 1  2  2  1
'''