import sys
input = sys.stdin.readline

N = int(input().strip())
x1x2 = [list(map(int, input().strip().split())) for _ in range(N)]

arr = [0] * 201
min_val = sys.maxsize
for x1, x2 in x1x2:
    if x1 < 0 or x2 < 0:
        min_x = min(x1, x2)
        min_val = min(min_val,min_x)

for x1, x2 in x1x2:
    if min_val > sys.maxsize:
        x1 += min_val
        x2 += min_val
    # print(range(x1, x2))
    for i in range(x1, x2):
        arr[i] += 1
# print(arr)
print(max(arr))


'''
    2 12
    9 10
    0 8
    10 11
    9 10
    
    0 1 2 3 4 5 6 7 8 9 10 11 12
    0 0 1 1 1 1 1 1 1 1 1  1  0
    0 0 0 0 0 0 0 0 0 1 0  0  0
    1 1 1 1 1 1 1 1 0 0 0  0  0
    0 0 0 0 0 0 0 0 0 0 1  0  0
    0 0 0 0 0 0 0 0 0 1 0  0  0
    1 1 2 2 2 2 2 2 1 3 2  1  0
'''
