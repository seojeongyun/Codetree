N = int(input())
A = list(map(int, input().split()))

# Please write your code here.
'''
N마리 소 1부터 N까지
i 소의 키는 Ai
서로 다른 세 소 위치 (i,j,k)
i<j<k and Ai<Aj<Ak 동시 만족 개수 구하기
'''
ans = 0
for i in range(N):
    for j in range(i+1,N):
        if A[i] <= A[j]:
            for k in range(j+1,N):
                if A[i] <= A[j] <= A[k]:
                    ans += 1
print(ans)