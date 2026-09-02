import sys

N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
# N개의 밭의 높이가 주어지면 연속하게 최소 T번 이상 H 높이로 나오게끔할 때 최소 비용

answer = sys.maxsize
gt = [H] * len(arr)

for i in range(N-T+1):
    expense = 0
    for j in range(i, i+T):
        expense += abs(arr[j]-gt[j])

    answer = min(answer, expense)

print(answer)

    