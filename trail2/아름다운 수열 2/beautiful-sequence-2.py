N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
# A에서 part select 하고 sort
answer = 0
for i in range(N):
    for j in range(i, N):
        lst = []
        for k in range(i, j+1):
            lst.append(A[k])
        if sorted(lst) == sorted(B):
            answer += 1

print(answer)