import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
cmd = [list(map(int, input().strip().split())) for _ in range(K)]

arr = [0] * (N+1)
for A, B in cmd:
    for i in range(A, B+1):
        arr[i] += 1

print(max(arr))