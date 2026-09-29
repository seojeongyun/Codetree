A = input()

# Please write your code here.
'''
문자열 A에서 (,)가 쌍을 이룰 수 있는 서로 다른 가짓수
여는 괄호가 먼저 나와야함
'''
ans = 0
for i, s in enumerate(A):
    if s == '(':
        for j in range(i,len(A)):
            if A[j] == ')':
                ans+= 1
print(ans)