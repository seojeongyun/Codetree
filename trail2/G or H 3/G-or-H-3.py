# K > x_i인 경우가 존재할 수 있다.
import sys

MAX_SIZE = 10000

n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
arr = [0] * (MAX_SIZE+1)
lst = list(zip(x,c))
for position, character in lst:
    if character == 'G':
        arr[position] = 1
    else:
        arr[position] = 2

answer = -sys.maxsize
for i in range(len(arr)-k):
    # print(arr)
    # print(i, i+k)
    answer = max(answer, sum(arr[i:i+k+1]))

print(answer)
