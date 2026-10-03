import sys
input = sys.stdin.readline

def drop():
    for i in range(len(arr)-1, -1, -1):
        if arr[i]:
            temp_arr.append(arr[i])
    arr[:] = temp_arr[::-1]

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
removed = [list(map(int, input().strip().split())) for _ in range(2)]

for start, end in removed:
    start, end = start-1, end-1
    # temp_arr
    temp_arr = []
    #
    arr[start:end+1] = [0] * (len(arr[start:end+1]))
    drop()

print(len(arr))
for i in arr:
    print(i)