import sys

n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

# 그룹이 겹치지 않으면서 N개의 그룹을 만드는 경우에 대해, 각 경우에 대해 그룹의 최댓값이 최소가 되는 값을 return

# 1. 그룹이 겹치지 않아야한다.
# 2. N개의 그룹을 만드는 경우의 수를 구해야한다.
    

nums.sort()
group = []
max_val = -sys.maxsize

for i in range(n):
    group.append([nums[i], nums[-1-i]])

for g in group:
    max_val = max(max_val, sum(g))

print(max_val)