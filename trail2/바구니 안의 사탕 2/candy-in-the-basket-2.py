MAX_SIZE = 400 # [200-200, 200+200] = [0, 400]
N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
answer = 0

def in_range(c, K, N):
    # print(c-K, c+K+1)
    return c-K >= 0 and c+K <=MAX_SIZE

arr = [0] * (MAX_SIZE+1)
data = list(zip(pos, candy))
for position, candy in data:
    arr[position] += candy

for C in range(200+1): # C의 MAX는 200
    max_val = 0
    if in_range(C, K, N):
        for i in range(C-K, C+K+1):
            max_val += arr[i]
        answer = max(answer, max_val)

print(answer)