n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
'''
N개의 집, x=1 ~ x=N
i번째 집 Ai명 사람
N개의 집 중 1곳으로 모임
모든 사람들의 이동거리 합 최소
'''
import sys
dist = 1000000

for i in range(1,n+1):
    home = i
    tmp = 0
    for j in range(1, n+1):
        tmp += abs((i-j))*A[j-1]
    dist = min(dist,tmp)
print(dist)
