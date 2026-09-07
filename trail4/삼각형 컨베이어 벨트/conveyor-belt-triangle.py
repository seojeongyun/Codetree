import sys
input = sys.stdin.readline

N, T = map(int, input().strip().split())
left = list(map(int, input().strip().split()))
right = list(map(int, input().strip().split()))
bottom = list(map(int, input().strip().split()))

bottom_ = bottom[::-1]

for _ in range(T):
    # rotate 되는 지점에 있는 값 저장
    left_tmp = left[-1]
    right_tmp = right[-1]


    # 각 배열 내에서 우측으로 한 칸 씩 이동
    left = [bottom_[0]] + left[:-1]
    right = [left_tmp] + right[:-1]
    bottom_ = bottom_[1:] + [right_tmp]

print(*left)
print(*right)
print(*bottom_[::-1])